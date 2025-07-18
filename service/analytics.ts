
import AsyncStorage from '@react-native-async-storage/async-storage';

interface UserSession {
  sessionId: string;
  startTime: Date;
  endTime?: Date;
  activitiesCompleted: number;
  xpEarned: number;
  mistakesCount: number;
  averageAccuracy: number;
}

interface LearningMetrics {
  totalStudyTime: number; // em minutos
  lessonsCompleted: number;
  averageSessionTime: number;
  streakDays: number;
  weakestSkills: string[];
  strongestSkills: string[];
  dailyGoalCompletion: number;
  weeklyProgress: number;
}

class AnalyticsService {
  private currentSession: UserSession | null = null;

  async startSession(): Promise<string> {
    const sessionId = `session_${Date.now()}`;
    this.currentSession = {
      sessionId,
      startTime: new Date(),
      activitiesCompleted: 0,
      xpEarned: 0,
      mistakesCount: 0,
      averageAccuracy: 0,
    };
    
    await this.saveSession();
    return sessionId;
  }

  async endSession(): Promise<void> {
    if (!this.currentSession) return;
    
    this.currentSession.endTime = new Date();
    await this.saveSession();
    await this.updateUserMetrics();
    this.currentSession = null;
  }

  async trackActivity(activityType: string, success: boolean, accuracy: number, xpGained: number): Promise<void> {
    if (!this.currentSession) return;

    this.currentSession.activitiesCompleted += 1;
    this.currentSession.xpEarned += xpGained;
    
    if (!success) {
      this.currentSession.mistakesCount += 1;
    }

    // Update running average accuracy
    const currentAvg = this.currentSession.averageAccuracy;
    const count = this.currentSession.activitiesCompleted;
    this.currentSession.averageAccuracy = (currentAvg * (count - 1) + accuracy) / count;

    await this.saveSession();
    
    // Track specific activity for learning insights
    await this.trackLearningPattern(activityType, accuracy);
  }

  async getUserMetrics(): Promise<LearningMetrics> {
    const stored = await AsyncStorage.getItem('user_metrics');
    if (stored) {
      return JSON.parse(stored);
    }

    // Default metrics
    return {
      totalStudyTime: 0,
      lessonsCompleted: 0,
      averageSessionTime: 0,
      streakDays: 0,
      weakestSkills: [],
      strongestSkills: [],
      dailyGoalCompletion: 0,
      weeklyProgress: 0,
    };
  }

  async getWeeklyReport(): Promise<any> {
    const sessions = await this.getRecentSessions(7);
    const metrics = await this.getUserMetrics();
    
    const totalTime = sessions.reduce((sum, session) => {
      if (session.endTime) {
        const duration = new Date(session.endTime).getTime() - new Date(session.startTime).getTime();
        return sum + duration / (1000 * 60); // convert to minutes
      }
      return sum;
    }, 0);

    const totalXP = sessions.reduce((sum, session) => sum + session.xpEarned, 0);
    const totalAccuracy = sessions.reduce((sum, session) => sum + session.averageAccuracy, 0) / sessions.length;

    return {
      weeklyStudyTime: Math.round(totalTime),
      weeklyXP: totalXP,
      averageAccuracy: Math.round(totalAccuracy),
      sessionsCount: sessions.length,
      improvementAreas: await this.getImprovementAreas(),
      achievements: await this.getWeeklyAchievements(),
    };
  }

  private async saveSession(): Promise<void> {
    if (!this.currentSession) return;
    
    const sessions = await this.getAllSessions();
    const updatedSessions = sessions.filter(s => s.sessionId !== this.currentSession!.sessionId);
    updatedSessions.push(this.currentSession);
    
    await AsyncStorage.setItem('user_sessions', JSON.stringify(updatedSessions));
  }

  private async getAllSessions(): Promise<UserSession[]> {
    const stored = await AsyncStorage.getItem('user_sessions');
    return stored ? JSON.parse(stored) : [];
  }

  private async getRecentSessions(days: number): Promise<UserSession[]> {
    const sessions = await this.getAllSessions();
    const cutoffDate = new Date();
    cutoffDate.setDate(cutoffDate.getDate() - days);
    
    return sessions.filter(session => 
      new Date(session.startTime) >= cutoffDate
    );
  }

  private async updateUserMetrics(): Promise<void> {
    const metrics = await this.getUserMetrics();
    const recentSessions = await this.getRecentSessions(30);
    
    // Update metrics based on recent sessions
    const totalTime = recentSessions.reduce((sum, session) => {
      if (session.endTime) {
        const duration = new Date(session.endTime).getTime() - new Date(session.startTime).getTime();
        return sum + duration / (1000 * 60);
      }
      return sum;
    }, 0);

    metrics.totalStudyTime = Math.round(totalTime);
    metrics.lessonsCompleted = recentSessions.reduce((sum, session) => sum + session.activitiesCompleted, 0);
    metrics.averageSessionTime = recentSessions.length > 0 ? totalTime / recentSessions.length : 0;

    await AsyncStorage.setItem('user_metrics', JSON.stringify(metrics));
  }

  private async trackLearningPattern(activityType: string, accuracy: number): Promise<void> {
    const patterns = await AsyncStorage.getItem('learning_patterns') || '{}';
    const data = JSON.parse(patterns);
    
    if (!data[activityType]) {
      data[activityType] = [];
    }
    
    data[activityType].push({
      timestamp: new Date().toISOString(),
      accuracy: accuracy,
    });
    
    // Keep only last 50 entries per activity type
    if (data[activityType].length > 50) {
      data[activityType] = data[activityType].slice(-50);
    }
    
    await AsyncStorage.setItem('learning_patterns', JSON.stringify(data));
  }

  private async getImprovementAreas(): Promise<string[]> {
    const patterns = await AsyncStorage.getItem('learning_patterns') || '{}';
    const data = JSON.parse(patterns);
    
    const areas = [];
    for (const [activity, records] of Object.entries(data) as [string, any[]][]) {
      const recentAccuracy = records.slice(-10).reduce((sum, r) => sum + r.accuracy, 0) / Math.min(10, records.length);
      if (recentAccuracy < 70) {
        areas.push(activity);
      }
    }
    
    return areas;
  }

  private async getWeeklyAchievements(): Promise<string[]> {
    // This would integrate with the achievement system
    return [];
  }
}

export const analytics = new AnalyticsService();

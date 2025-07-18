
import AsyncStorage from '@react-native-async-storage/async-storage';

const API_BASE_URL = 'https://your-backend-url.com'; // Replace with your backend URL

interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

interface AudioAnalysis {
  overall_score: number;
  pronunciation_score: number;
  fluency_score: number;
  accuracy_score: number;
  transcription: string;
  feedback: string;
  suggestions: string[];
  ai_insights: string[];
  next_steps: string[];
  real_time_feedback: string[];
  learning_insights: {
    learning_velocity: string;
    strength_areas: string[];
    focus_areas: string[];
    recommended_practice: string[];
    next_milestone: string;
  };
  processing_time: number;
  model_confidence: number;
}

interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
  timestamp: string;
}

interface ChatResponse {
  response: string;
  follow_up_questions: string[];
  context_understanding: any;
  suggested_exercises: any[];
  confidence_level: number;
}

interface LessonData {
  lesson_id: string;
  title: string;
  difficulty: string;
  exercises: any[];
  focus_areas: string[];
  estimated_duration: number;
  success_probability: number;
}

interface UserProgress {
  total_sessions: number;
  total_practice_time: string;
  average_session_duration: string;
  pronunciation_improvement: number;
  fluency_score: number;
  consistency_streak: number;
  favorite_practice_time: string;
  most_improved_area: string;
  recent_achievements: string[];
}

class BilingualAIApiService {
  private baseUrl: string;
  private token: string | null = null;

  constructor(baseUrl: string = API_BASE_URL) {
    this.baseUrl = baseUrl;
    this.initializeAuth();
  }

  private async initializeAuth(): Promise<void> {
    try {
      const token = await AsyncStorage.getItem('auth_token');
      this.token = token;
    } catch (error) {
      console.error('Failed to initialize auth:', error);
    }
  }

  private async getAuthHeaders(): Promise<Record<string, string>> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (this.token) {
      headers.Authorization = `Bearer ${this.token}`;
    }

    return headers;
  }

  private async makeRequest<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<ApiResponse<T>> {
    try {
      const url = `${this.baseUrl}${endpoint}`;
      const headers = await this.getAuthHeaders();

      const response = await fetch(url, {
        ...options,
        headers: {
          ...headers,
          ...options.headers,
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return {
        success: true,
        data,
      };
    } catch (error) {
      console.error('API request failed:', error);
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Unknown error',
      };
    }
  }

  // Authentication
  async login(email: string, password: string): Promise<ApiResponse<{ token: string; user: any }>> {
    const response = await this.makeRequest<{ token: string; user: any }>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });

    if (response.success && response.data) {
      this.token = response.data.token;
      await AsyncStorage.setItem('auth_token', this.token);
    }

    return response;
  }

  async logout(): Promise<void> {
    this.token = null;
    await AsyncStorage.removeItem('auth_token');
  }

  // Advanced Audio Processing
  async submitAudioForAnalysis(
    audioUri: string,
    targetPhrase: string,
    difficulty: string = 'intermediate',
    lessonContext: string = ''
  ): Promise<ApiResponse<AudioAnalysis>> {
    try {
      const formData = new FormData();
      formData.append('file', {
        uri: audioUri,
        type: 'audio/wav',
        name: 'audio.wav',
      } as any);
      formData.append('target_phrase', targetPhrase);
      formData.append('difficulty', difficulty);
      formData.append('lesson_context', lessonContext);

      const headers = await this.getAuthHeaders();
      delete headers['Content-Type']; // Let FormData set the content type

      const response = await fetch(`${this.baseUrl}/audio/submit`, {
        method: 'POST',
        headers,
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return {
        success: true,
        data: data.analysis,
      };
    } catch (error) {
      console.error('Audio submission failed:', error);
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Audio submission failed',
      };
    }
  }

  async transcribeAudio(audioUri: string, language: string = 'en'): Promise<ApiResponse<any>> {
    try {
      const formData = new FormData();
      formData.append('file', {
        uri: audioUri,
        type: 'audio/wav',
        name: 'audio.wav',
      } as any);
      formData.append('language', language);

      const headers = await this.getAuthHeaders();
      delete headers['Content-Type'];

      const response = await fetch(`${this.baseUrl}/audio/transcribe`, {
        method: 'POST',
        headers,
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return {
        success: true,
        data: data.transcription,
      };
    } catch (error) {
      console.error('Transcription failed:', error);
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Transcription failed',
      };
    }
  }

  async analyzePronunciation(audioUri: string, targetText: string): Promise<ApiResponse<any>> {
    try {
      const formData = new FormData();
      formData.append('file', {
        uri: audioUri,
        type: 'audio/wav',
        name: 'audio.wav',
      } as any);
      formData.append('target_text', targetText);

      const headers = await this.getAuthHeaders();
      delete headers['Content-Type'];

      const response = await fetch(`${this.baseUrl}/audio/pronunciation-analysis`, {
        method: 'POST',
        headers,
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return {
        success: true,
        data: data.pronunciation_analysis,
      };
    } catch (error) {
      console.error('Pronunciation analysis failed:', error);
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Pronunciation analysis failed',
      };
    }
  }

  // Advanced AI Chat
  async sendChatMessage(
    messages: ChatMessage[],
    context: string = '',
    personality: string = 'friendly_teacher'
  ): Promise<ApiResponse<ChatResponse>> {
    return this.makeRequest<ChatResponse>('/chat/chat', {
      method: 'POST',
      body: JSON.stringify({
        messages,
        context,
        personality,
      }),
    });
  }

  async generateLessonDialogue(
    topic: string,
    difficulty: string,
    userProfile: any
  ): Promise<ApiResponse<any>> {
    return this.makeRequest<any>('/chat/lesson-dialogue', {
      method: 'POST',
      body: JSON.stringify({
        topic,
        difficulty,
        user_profile: userProfile,
      }),
    });
  }

  async provideGrammarFeedback(
    userText: string,
    targetGrammar: string
  ): Promise<ApiResponse<any>> {
    return this.makeRequest<any>('/chat/grammar-feedback', {
      method: 'POST',
      body: JSON.stringify({
        user_text: userText,
        target_grammar: targetGrammar,
      }),
    });
  }

  // Personalized Lessons
  async generatePersonalizedLesson(
    userProfile: any,
    performanceHistory: any[]
  ): Promise<ApiResponse<LessonData>> {
    return this.makeRequest<LessonData>('/lessons/personalized', {
      method: 'POST',
      body: JSON.stringify({
        user_profile: userProfile,
        performance_history: performanceHistory,
      }),
    });
  }

  async getAdaptiveLessons(difficulty: string): Promise<ApiResponse<any[]>> {
    return this.makeRequest<any[]>(`/lessons/adaptive?difficulty=${difficulty}`);
  }

  async submitLessonAnswer(
    lessonId: string,
    answer: string,
    exerciseType: string
  ): Promise<ApiResponse<any>> {
    return this.makeRequest<any>('/lessons/submit-answer', {
      method: 'POST',
      body: JSON.stringify({
        lesson_id: lessonId,
        answer,
        exercise_type: exerciseType,
      }),
    });
  }

  // User Progress & Analytics
  async getUserProgress(userId: string): Promise<ApiResponse<UserProgress>> {
    return this.makeRequest<UserProgress>(`/progress/user/${userId}`);
  }

  async getDetailedAnalytics(userId: string): Promise<ApiResponse<any>> {
    return this.makeRequest<any>(`/progress/analytics/${userId}`);
  }

  async getUserAudioStats(userId: string): Promise<ApiResponse<any>> {
    return this.makeRequest<any>(`/audio/user-audio-stats/${userId}`);
  }

  async getLeaderboard(timeFrame: string = 'week'): Promise<ApiResponse<any[]>> {
    return this.makeRequest<any[]>(`/progress/leaderboard?timeframe=${timeFrame}`);
  }

  // Real-time Features
  async getRealTimeFeedback(audioChunk: any, context: any): Promise<ApiResponse<any>> {
    try {
      const formData = new FormData();
      formData.append('file', audioChunk);
      formData.append('context', JSON.stringify(context));

      const headers = await this.getAuthHeaders();
      delete headers['Content-Type'];

      const response = await fetch(`${this.baseUrl}/audio/real-time-feedback`, {
        method: 'POST',
        headers,
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return {
        success: true,
        data: data.real_time_feedback,
      };
    } catch (error) {
      console.error('Real-time feedback failed:', error);
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Real-time feedback failed',
      };
    }
  }

  // System Status
  async getSystemStatus(): Promise<ApiResponse<any>> {
    return this.makeRequest<any>('/health');
  }

  async getAIStatus(): Promise<ApiResponse<any>> {
    return this.makeRequest<any>('/ai-status');
  }

  // Conversation Topics
  async generateConversationTopics(
    userInterests: string[],
    difficulty: string
  ): Promise<ApiResponse<any[]>> {
    return this.makeRequest<any[]>('/chat/conversation-topics', {
      method: 'POST',
      body: JSON.stringify({
        user_interests: userInterests,
        difficulty,
      }),
    });
  }

  async analyzeConversationFlow(conversationHistory: any[]): Promise<ApiResponse<any>> {
    return this.makeRequest<any>('/chat/analyze-conversation', {
      method: 'POST',
      body: JSON.stringify({
        conversation_history: conversationHistory,
      }),
    });
  }

  // Gamification
  async getUserAchievements(userId: string): Promise<ApiResponse<any[]>> {
    return this.makeRequest<any[]>(`/progress/achievements/${userId}`);
  }

  async updateUserStreak(userId: string): Promise<ApiResponse<any>> {
    return this.makeRequest<any>(`/progress/streak/${userId}`, {
      method: 'POST',
    });
  }

  async getXPHistory(userId: string): Promise<ApiResponse<any[]>> {
    return this.makeRequest<any[]>(`/progress/xp-history/${userId}`);
  }
}

// Export singleton instance
export const bilingualAIApi = new BilingualAIApiService();
export default bilingualAIApi;

// Export types for use in components
export type {
  AudioAnalysis,
  ChatMessage,
  ChatResponse,
  LessonData,
  UserProgress,
  ApiResponse,
};


import { useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface StreakData {
  currentStreak: number;
  longestStreak: number;
  lastActivityDate: string;
  weeklyGoal: number;
  weeklyProgress: number;
}

export const useStreakSystem = () => {
  const [streakData, setStreakData] = useState<StreakData>({
    currentStreak: 0,
    longestStreak: 0,
    lastActivityDate: '',
    weeklyGoal: 7,
    weeklyProgress: 0
  });

  const updateStreak = async () => {
    const today = new Date().toDateString();
    const stored = await AsyncStorage.getItem('streakData');
    const data = stored ? JSON.parse(stored) : streakData;
    
    const lastDate = new Date(data.lastActivityDate);
    const todayDate = new Date(today);
    const diffTime = todayDate.getTime() - lastDate.getTime();
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

    if (diffDays === 1) {
      // Consecutive day
      data.currentStreak += 1;
      data.longestStreak = Math.max(data.longestStreak, data.currentStreak);
    } else if (diffDays > 1) {
      // Streak broken
      data.currentStreak = 1;
    }
    // Same day = maintain streak

    data.lastActivityDate = today;
    data.weeklyProgress = Math.min(data.weeklyProgress + 1, data.weeklyGoal);
    
    await AsyncStorage.setItem('streakData', JSON.stringify(data));
    setStreakData(data);
  };

  const resetWeeklyProgress = async () => {
    const updated = { ...streakData, weeklyProgress: 0 };
    await AsyncStorage.setItem('streakData', JSON.stringify(updated));
    setStreakData(updated);
  };

  useEffect(() => {
    const loadStreak = async () => {
      const stored = await AsyncStorage.getItem('streakData');
      if (stored) {
        setStreakData(JSON.parse(stored));
      }
    };
    loadStreak();
  }, []);

  return { streakData, updateStreak, resetWeeklyProgress };
};


import React, { useState, useEffect } from 'react';
import { View, StyleSheet, Modal, ScrollView, TouchableOpacity, Animated } from 'react-native';
import { useThemeColor } from '@/hooks/useThemeColor';
import Typography from './Typography';
import { Ionicons } from '@expo/vector-icons';

interface Achievement {
  id: string;
  title: string;
  description: string;
  icon: string;
  progress: number;
  maxProgress: number;
  unlocked: boolean;
  rarity: 'common' | 'rare' | 'epic' | 'legendary';
  xpReward: number;
}

interface AchievementSystemProps {
  userXP: number;
  perfectStreak: number;
  currentDifficulty: string;
}

export const AchievementSystem = ({ userXP, perfectStreak, currentDifficulty }: AchievementSystemProps) => {
  const [achievements, setAchievements] = useState<Achievement[]>([]);
  const [showModal, setShowModal] = useState(false);
  const [newUnlocks, setNewUnlocks] = useState<Achievement[]>([]);
  
  const backgroundColor = useThemeColor({}, 'background');
  const tintColor = useThemeColor({}, 'tint');
  const textColor = useThemeColor({}, 'text');

  const achievementDatabase: Achievement[] = [
    {
      id: 'first_steps',
      title: 'Primeiros Passos',
      description: 'Complete sua primeira prática de fala',
      icon: '👶',
      progress: Math.min(userXP > 0 ? 1 : 0, 1),
      maxProgress: 1,
      unlocked: userXP > 0,
      rarity: 'common',
      xpReward: 50,
    },
    {
      id: 'perfectionist',
      title: 'Perfeccionista',
      description: 'Obtenha 3 pronúncias perfeitas seguidas',
      icon: '🎯',
      progress: Math.min(perfectStreak, 3),
      maxProgress: 3,
      unlocked: perfectStreak >= 3,
      rarity: 'rare',
      xpReward: 150,
    },
    {
      id: 'ai_whisperer',
      title: 'Sussurrador de IA',
      description: 'Alcance 95% de precisão com IA avançada',
      icon: '🤖',
      progress: 0, // This would be tracked separately
      maxProgress: 1,
      unlocked: false,
      rarity: 'epic',
      xpReward: 300,
    },
    {
      id: 'polyglot_master',
      title: 'Mestre Poliglota',
      description: 'Domine todos os níveis de dificuldade',
      icon: '🌍',
      progress: currentDifficulty === 'advanced' ? 3 : currentDifficulty === 'intermediate' ? 2 : 1,
      maxProgress: 3,
      unlocked: currentDifficulty === 'advanced',
      rarity: 'legendary',
      xpReward: 500,
    },
    {
      id: 'consistent_learner',
      title: 'Aprendiz Consistente',
      description: 'Mantenha uma sequência de 7 dias',
      icon: '🔥',
      progress: Math.min(userXP > 1000 ? 7 : 0, 7), // Simplified tracking
      maxProgress: 7,
      unlocked: userXP > 1000,
      rarity: 'rare',
      xpReward: 200,
    },
    {
      id: 'xp_collector',
      title: 'Coletor de XP',
      description: 'Acumule 2000 pontos de experiência',
      icon: '⭐',
      progress: Math.min(userXP, 2000),
      maxProgress: 2000,
      unlocked: userXP >= 2000,
      rarity: 'common',
      xpReward: 100,
    },
  ];

  useEffect(() => {
    const updatedAchievements = achievementDatabase.map(achievement => ({
      ...achievement,
      progress: getUpdatedProgress(achievement),
      unlocked: checkUnlocked(achievement),
    }));

    const previouslyLocked = achievements.filter(a => !a.unlocked).map(a => a.id);
    const newlyUnlocked = updatedAchievements.filter(a => 
      a.unlocked && previouslyLocked.includes(a.id)
    );

    if (newlyUnlocked.length > 0) {
      setNewUnlocks(newlyUnlocked);
      setShowModal(true);
    }

    setAchievements(updatedAchievements);
  }, [userXP, perfectStreak, currentDifficulty]);

  const getUpdatedProgress = (achievement: Achievement) => {
    switch (achievement.id) {
      case 'first_steps':
        return Math.min(userXP > 0 ? 1 : 0, 1);
      case 'perfectionist':
        return Math.min(perfectStreak, 3);
      case 'polyglot_master':
        return currentDifficulty === 'advanced' ? 3 : currentDifficulty === 'intermediate' ? 2 : 1;
      case 'consistent_learner':
        return Math.min(userXP > 1000 ? 7 : Math.floor(userXP / 150), 7);
      case 'xp_collector':
        return Math.min(userXP, 2000);
      default:
        return achievement.progress;
    }
  };

  const checkUnlocked = (achievement: Achievement) => {
    switch (achievement.id) {
      case 'first_steps':
        return userXP > 0;
      case 'perfectionist':
        return perfectStreak >= 3;
      case 'polyglot_master':
        return currentDifficulty === 'advanced';
      case 'consistent_learner':
        return userXP > 1000;
      case 'xp_collector':
        return userXP >= 2000;
      default:
        return achievement.unlocked;
    }
  };

  const getRarityColor = (rarity: string) => {
    const colors = {
      common: '#9E9E9E',
      rare: '#2196F3',
      epic: '#9C27B0',
      legendary: '#FF9800',
    };
    return colors[rarity as keyof typeof colors] || colors.common;
  };

  const getProgressPercentage = (achievement: Achievement) => {
    return (achievement.progress / achievement.maxProgress) * 100;
  };

  return (
    <View style={styles.container}>
      <TouchableOpacity 
        style={[styles.header, { backgroundColor: tintColor + '20' }]}
        onPress={() => setShowModal(true)}
      >
        <Typography type="subtitle">
          <Ionicons name="trophy" size={16} /> Conquistas
        </Typography>
        <Typography type="default">
          {achievements.filter(a => a.unlocked).length}/{achievements.length} desbloqueadas
        </Typography>
      </TouchableOpacity>

      <Modal
        visible={showModal}
        animationType="slide"
        presentationStyle="pageSheet"
        onRequestClose={() => setShowModal(false)}
      >
        <View style={[styles.modalContainer, { backgroundColor }]}>
          <View style={styles.modalHeader}>
            <Typography type="title">🏆 Suas Conquistas</Typography>
            <TouchableOpacity
              onPress={() => setShowModal(false)}
              style={styles.closeButton}
            >
              <Ionicons name="close" size={24} color={textColor} />
            </TouchableOpacity>
          </View>

          <ScrollView style={styles.achievementsList}>
            {achievements.map((achievement) => (
              <View
                key={achievement.id}
                style={[
                  styles.achievementCard,
                  {
                    borderColor: getRarityColor(achievement.rarity),
                    opacity: achievement.unlocked ? 1 : 0.6,
                  }
                ]}
              >
                <View style={styles.achievementContent}>
                  <View style={styles.achievementIcon}>
                    <Typography type="title">{achievement.icon}</Typography>
                  </View>
                  
                  <View style={styles.achievementInfo}>
                    <Typography type="subtitle">{achievement.title}</Typography>
                    <Typography type="default" style={styles.achievementDescription}>
                      {achievement.description}
                    </Typography>
                    
                    <View style={styles.progressContainer}>
                      <View style={[styles.progressBar, { backgroundColor: '#E0E0E0' }]}>
                        <View
                          style={[
                            styles.progressFill,
                            {
                              backgroundColor: getRarityColor(achievement.rarity),
                              width: `${getProgressPercentage(achievement)}%`,
                            }
                          ]}
                        />
                      </View>
                      <Typography type="default" style={styles.progressText}>
                        {achievement.progress}/{achievement.maxProgress}
                      </Typography>
                    </View>
                    
                    <View style={styles.rewardContainer}>
                      <Typography type="default" style={[styles.rarityBadge, { color: getRarityColor(achievement.rarity) }]}>
                        {achievement.rarity.toUpperCase()}
                      </Typography>
                      <Typography type="default">+{achievement.xpReward} XP</Typography>
                    </View>
                  </View>
                  
                  {achievement.unlocked && (
                    <View style={styles.unlockedBadge}>
                      <Ionicons name="checkmark-circle" size={24} color="#4CAF50" />
                    </View>
                  )}
                </View>
              </View>
            ))}
          </ScrollView>
        </View>
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    margin: 16,
  },
  header: {
    padding: 16,
    borderRadius: 12,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  modalContainer: {
    flex: 1,
    paddingTop: 50,
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
  },
  closeButton: {
    padding: 8,
  },
  achievementsList: {
    flex: 1,
    padding: 16,
  },
  achievementCard: {
    borderWidth: 2,
    borderRadius: 12,
    marginBottom: 12,
    overflow: 'hidden',
  },
  achievementContent: {
    flexDirection: 'row',
    padding: 16,
    alignItems: 'center',
  },
  achievementIcon: {
    marginRight: 16,
  },
  achievementInfo: {
    flex: 1,
  },
  achievementDescription: {
    opacity: 0.7,
    marginBottom: 8,
  },
  progressContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  progressBar: {
    flex: 1,
    height: 6,
    borderRadius: 3,
    overflow: 'hidden',
    marginRight: 8,
  },
  progressFill: {
    height: '100%',
    borderRadius: 3,
  },
  progressText: {
    fontSize: 12,
    minWidth: 40,
  },
  rewardContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  rarityBadge: {
    fontSize: 12,
    fontWeight: 'bold',
  },
  unlockedBadge: {
    marginLeft: 8,
  },
});


import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, FlatList } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { Colors } from '@/constants/Colors';
import { useColorScheme } from '@/hooks/useColorScheme';

interface User {
  id: string;
  name: string;
  avatar: string;
  level: number;
  xp: number;
  streak: number;
  country: string;
  isOnline: boolean;
}

interface Challenge {
  id: string;
  title: string;
  description: string;
  type: 'vocabulary' | 'pronunciation' | 'conversation' | 'speed';
  participants: number;
  maxParticipants: number;
  reward: number;
  difficulty: 'easy' | 'medium' | 'hard';
  timeLimit: string;
  status: 'waiting' | 'active' | 'completed';
}

interface SocialLearningHubProps {
  currentUser: User;
}

export function SocialLearningHub({ currentUser }: SocialLearningHubProps) {
  const colorScheme = useColorScheme();
  const colors = Colors[colorScheme ?? 'light'];
  const [activeTab, setActiveTab] = useState<'leaderboard' | 'challenges' | 'friends'>('leaderboard');
  const [leaderboard, setLeaderboard] = useState<User[]>([]);
  const [challenges, setChallenges] = useState<Challenge[]>([]);
  const [friends, setFriends] = useState<User[]>([]);

  useEffect(() => {
    loadSocialData();
  }, []);

  const loadSocialData = async () => {
    // Simular dados do leaderboard
    setLeaderboard([
      {
        id: '1',
        name: 'Maria Silva',
        avatar: '👩‍💼',
        level: 25,
        xp: 12500,
        streak: 15,
        country: '🇧🇷',
        isOnline: true
      },
      {
        id: '2', 
        name: 'João Santos',
        avatar: '👨‍💻',
        level: 23,
        xp: 11800,
        streak: 12,
        country: '🇧🇷',
        isOnline: false
      },
      {
        id: '3',
        name: 'Ana Costa',
        avatar: '👩‍🎓',
        level: 22,
        xp: 11200,
        streak: 8,
        country: '🇧🇷',
        isOnline: true
      }
    ]);

    // Simular desafios disponíveis
    setChallenges([
      {
        id: 'ch1',
        title: '🏆 Duelo de Vocabulário',
        description: 'Teste seu vocabulário contra outros jogadores em tempo real',
        type: 'vocabulary',
        participants: 3,
        maxParticipants: 8,
        reward: 500,
        difficulty: 'medium',
        timeLimit: '10 min',
        status: 'waiting'
      },
      {
        id: 'ch2',
        title: '🎤 Batalha de Pronúncia',
        description: 'Quem pronuncia melhor as palavras difíceis?',
        type: 'pronunciation',
        participants: 1,
        maxParticipants: 4,
        reward: 300,
        difficulty: 'hard',
        timeLimit: '15 min',
        status: 'waiting'
      },
      {
        id: 'ch3',
        title: '⚡ Speed Challenge',
        description: 'Responda o máximo de perguntas em 2 minutos',
        type: 'speed',
        participants: 8,
        maxParticipants: 8,
        reward: 200,
        difficulty: 'easy',
        timeLimit: '2 min',
        status: 'active'
      }
    ]);

    // Simular lista de amigos
    setFriends([
      {
        id: 'f1',
        name: 'Carlos Mendes',
        avatar: '👨‍🏫',
        level: 18,
        xp: 9500,
        streak: 5,
        country: '🇧🇷',
        isOnline: true
      },
      {
        id: 'f2',
        name: 'Lucia Oliveira',
        avatar: '👩‍⚕️',
        level: 20,
        xp: 10200,
        streak: 7,
        country: '🇧🇷',
        isOnline: false
      }
    ]);
  };

  const joinChallenge = (challengeId: string) => {
    setChallenges(challenges.map(challenge => 
      challenge.id === challengeId 
        ? { ...challenge, participants: challenge.participants + 1 }
        : challenge
    ));
  };

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'easy': return '#4CAF50';
      case 'medium': return '#FF9800';
      case 'hard': return '#F44336';
      default: return colors.text;
    }
  };

  const renderLeaderboardItem = ({ item, index }: { item: User; index: number }) => (
    <View style={[styles.leaderboardItem, { backgroundColor: colors.background }]}>
      <View style={styles.rankContainer}>
        <Text style={[styles.rankText, { color: colors.text }]}>#{index + 1}</Text>
        {index < 3 && (
          <Text style={styles.medalEmoji}>
            {index === 0 ? '🥇' : index === 1 ? '🥈' : '🥉'}
          </Text>
        )}
      </View>
      
      <Text style={styles.avatarText}>{item.avatar}</Text>
      
      <View style={styles.userInfo}>
        <View style={styles.nameContainer}>
          <Text style={[styles.userName, { color: colors.text }]}>{item.name}</Text>
          <Text style={styles.countryFlag}>{item.country}</Text>
          {item.isOnline && <View style={styles.onlineIndicator} />}
        </View>
        <Text style={[styles.userLevel, { color: colors.text + 'CC' }]}>
          Level {item.level} • {item.xp.toLocaleString()} XP
        </Text>
        <Text style={[styles.userStreak, { color: '#FF6B35' }]}>
          🔥 {item.streak} dias
        </Text>
      </View>
      
      <TouchableOpacity style={styles.challengeButton}>
        <Ionicons name="flash" size={16} color="#4CAF50" />
      </TouchableOpacity>
    </View>
  );

  const renderChallengeItem = ({ item }: { item: Challenge }) => (
    <View style={[styles.challengeCard, { backgroundColor: colors.background }]}>
      <View style={styles.challengeHeader}>
        <Text style={[styles.challengeTitle, { color: colors.text }]}>{item.title}</Text>
        <View style={[styles.difficultyBadge, { backgroundColor: getDifficultyColor(item.difficulty) }]}>
          <Text style={styles.difficultyText}>{item.difficulty}</Text>
        </View>
      </View>
      
      <Text style={[styles.challengeDescription, { color: colors.text + 'CC' }]}>
        {item.description}
      </Text>
      
      <View style={styles.challengeStats}>
        <View style={styles.statItem}>
          <Ionicons name="people" size={16} color={colors.text + 'CC'} />
          <Text style={[styles.statText, { color: colors.text + 'CC' }]}>
            {item.participants}/{item.maxParticipants}
          </Text>
        </View>
        
        <View style={styles.statItem}>
          <Ionicons name="time" size={16} color={colors.text + 'CC'} />
          <Text style={[styles.statText, { color: colors.text + 'CC' }]}>
            {item.timeLimit}
          </Text>
        </View>
        
        <View style={styles.statItem}>
          <Ionicons name="star" size={16} color="#FFD700" />
          <Text style={[styles.statText, { color: colors.text + 'CC' }]}>
            {item.reward} XP
          </Text>
        </View>
      </View>
      
      <TouchableOpacity
        style={[
          styles.joinButton,
          { 
            backgroundColor: item.status === 'waiting' ? '#4CAF50' : 
                           item.status === 'active' ? '#FF9800' : '#9E9E9E'
          }
        ]}
        onPress={() => item.status === 'waiting' && joinChallenge(item.id)}
        disabled={item.status !== 'waiting'}
      >
        <Text style={styles.joinButtonText}>
          {item.status === 'waiting' ? 'Participar' : 
           item.status === 'active' ? 'Em Andamento' : 'Finalizado'}
        </Text>
      </TouchableOpacity>
    </View>
  );

  return (
    <View style={[styles.container, { backgroundColor: colors.background }]}>
      <LinearGradient
        colors={['#667eea', '#764ba2']}
        style={styles.header}
      >
        <Text style={styles.headerTitle}>🌟 Hub Social</Text>
        <Text style={styles.headerSubtitle}>Conecte-se, compete e aprenda junto!</Text>
      </LinearGradient>

      <View style={styles.tabContainer}>
        {['leaderboard', 'challenges', 'friends'].map((tab) => (
          <TouchableOpacity
            key={tab}
            style={[
              styles.tabButton,
              { 
                backgroundColor: activeTab === tab ? '#4CAF50' : 'transparent',
                borderBottomColor: activeTab === tab ? '#4CAF50' : 'transparent'
              }
            ]}
            onPress={() => setActiveTab(tab as any)}
          >
            <Text style={[
              styles.tabText,
              { color: activeTab === tab ? 'white' : colors.text + 'CC' }
            ]}>
              {tab === 'leaderboard' ? '🏆 Ranking' :
               tab === 'challenges' ? '⚔️ Desafios' : '👥 Amigos'}
            </Text>
          </TouchableOpacity>
        ))}
      </View>

      <View style={styles.content}>
        {activeTab === 'leaderboard' && (
          <FlatList
            data={leaderboard}
            renderItem={renderLeaderboardItem}
            keyExtractor={(item) => item.id}
            showsVerticalScrollIndicator={false}
          />
        )}

        {activeTab === 'challenges' && (
          <FlatList
            data={challenges}
            renderItem={renderChallengeItem}
            keyExtractor={(item) => item.id}
            showsVerticalScrollIndicator={false}
          />
        )}

        {activeTab === 'friends' && (
          <FlatList
            data={friends}
            renderItem={renderLeaderboardItem}
            keyExtractor={(item) => item.id}
            showsVerticalScrollIndicator={false}
          />
        )}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  header: {
    padding: 20,
    paddingTop: 40,
  },
  headerTitle: {
    color: 'white',
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  headerSubtitle: {
    color: 'rgba(255,255,255,0.9)',
    fontSize: 16,
    textAlign: 'center',
    marginTop: 4,
  },
  tabContainer: {
    flexDirection: 'row',
    backgroundColor: 'rgba(0,0,0,0.05)',
  },
  tabButton: {
    flex: 1,
    paddingVertical: 16,
    borderBottomWidth: 3,
  },
  tabText: {
    textAlign: 'center',
    fontWeight: '600',
  },
  content: {
    flex: 1,
    padding: 16,
  },
  leaderboardItem: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 16,
    marginBottom: 12,
    borderRadius: 12,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
  },
  rankContainer: {
    alignItems: 'center',
    marginRight: 12,
    minWidth: 40,
  },
  rankText: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  medalEmoji: {
    fontSize: 16,
    marginTop: 2,
  },
  avatarText: {
    fontSize: 32,
    marginRight: 12,
  },
  userInfo: {
    flex: 1,
  },
  nameContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 2,
  },
  userName: {
    fontSize: 16,
    fontWeight: 'bold',
    marginRight: 8,
  },
  countryFlag: {
    fontSize: 14,
    marginRight: 4,
  },
  onlineIndicator: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#4CAF50',
  },
  userLevel: {
    fontSize: 14,
    marginBottom: 2,
  },
  userStreak: {
    fontSize: 12,
    fontWeight: '500',
  },
  challengeButton: {
    padding: 8,
  },
  challengeCard: {
    padding: 16,
    marginBottom: 16,
    borderRadius: 12,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
  },
  challengeHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  challengeTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    flex: 1,
  },
  difficultyBadge: {
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 12,
  },
  difficultyText: {
    color: 'white',
    fontSize: 10,
    fontWeight: 'bold',
    textTransform: 'uppercase',
  },
  challengeDescription: {
    fontSize: 14,
    marginBottom: 12,
    lineHeight: 20,
  },
  challengeStats: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 16,
  },
  statItem: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  statText: {
    fontSize: 12,
    marginLeft: 4,
  },
  joinButton: {
    paddingVertical: 12,
    borderRadius: 8,
    alignItems: 'center',
  },
  joinButtonText: {
    color: 'white',
    fontWeight: 'bold',
  },
});


import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { Colors } from '@/constants/Colors';
import { useColorScheme } from '@/hooks/useColorScheme';

interface LearningPath {
  id: string;
  title: string;
  description: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  progress: number;
  estimatedTime: string;
  skills: string[];
  isRecommended: boolean;
}

interface LearningPathSystemProps {
  userId: string;
  currentLevel: number;
  completedLessons: string[];
}

export function LearningPathSystem({ userId, currentLevel, completedLessons }: LearningPathSystemProps) {
  const colorScheme = useColorScheme();
  const colors = Colors[colorScheme ?? 'light'];
  const [learningPaths, setLearningPaths] = useState<LearningPath[]>([]);
  const [selectedPath, setSelectedPath] = useState<string | null>(null);

  useEffect(() => {
    generateAdaptivePaths();
  }, [currentLevel, completedLessons]);

  const generateAdaptivePaths = () => {
    // Gera caminhos adaptativos baseados no progresso do usuário
    const paths: LearningPath[] = [
      {
        id: 'conversation-basics',
        title: 'Conversação Básica',
        description: 'Aprenda frases essenciais para conversas do dia a dia',
        difficulty: 'beginner',
        progress: calculateProgress('conversation-basics'),
        estimatedTime: '2 semanas',
        skills: ['Cumprimentos', 'Apresentações', 'Pedidos básicos'],
        isRecommended: currentLevel <= 5
      },
      {
        id: 'business-english',
        title: 'Inglês para Negócios',
        description: 'Vocabulário e expressões para ambiente profissional',
        difficulty: 'intermediate',
        progress: calculateProgress('business-english'),
        estimatedTime: '4 semanas',
        skills: ['Reuniões', 'Apresentações', 'Emails formais'],
        isRecommended: currentLevel >= 10 && currentLevel <= 20
      },
      {
        id: 'advanced-pronunciation',
        title: 'Pronúncia Avançada',
        description: 'Aperfeiçoe sua pronúncia com técnicas avançadas',
        difficulty: 'advanced',
        progress: calculateProgress('advanced-pronunciation'),
        estimatedTime: '6 semanas',
        skills: ['Entonação', 'Sotaque', 'Fluência'],
        isRecommended: currentLevel >= 25
      }
    ];
    setLearningPaths(paths);
  };

  const calculateProgress = (pathId: string): number => {
    // Calcula progresso baseado nas lições completadas
    return Math.random() * 100; // Placeholder - implementar lógica real
  };

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'beginner': return '#4CAF50';
      case 'intermediate': return '#FF9800';
      case 'advanced': return '#F44336';
      default: return colors.text;
    }
  };

  const startLearningPath = (pathId: string) => {
    setSelectedPath(pathId);
    // Implementar navegação para primeira lição do caminho
  };

  return (
    <ScrollView style={[styles.container, { backgroundColor: colors.background }]}>
      <Text style={[styles.title, { color: colors.text }]}>
        🎯 Caminhos de Aprendizado Personalizados
      </Text>
      
      {learningPaths.map((path) => (
        <TouchableOpacity
          key={path.id}
          style={[
            styles.pathCard,
            { 
              backgroundColor: colors.background,
              borderColor: path.isRecommended ? '#4CAF50' : colors.text + '20'
            }
          ]}
          onPress={() => startLearningPath(path.id)}
        >
          <LinearGradient
            colors={path.isRecommended ? ['#4CAF50', '#45A049'] : [colors.background, colors.background]}
            style={styles.gradientHeader}
          >
            {path.isRecommended && (
              <View style={styles.recommendedBadge}>
                <Ionicons name="star" size={16} color="#FFD700" />
                <Text style={styles.recommendedText}>Recomendado</Text>
              </View>
            )}
          </LinearGradient>

          <View style={styles.pathContent}>
            <View style={styles.pathHeader}>
              <Text style={[styles.pathTitle, { color: colors.text }]}>{path.title}</Text>
              <View style={[styles.difficultyBadge, { backgroundColor: getDifficultyColor(path.difficulty) }]}>
                <Text style={styles.difficultyText}>{path.difficulty}</Text>
              </View>
            </View>

            <Text style={[styles.pathDescription, { color: colors.text + 'CC' }]}>
              {path.description}
            </Text>

            <View style={styles.progressContainer}>
              <View style={styles.progressBar}>
                <View 
                  style={[
                    styles.progressFill, 
                    { 
                      width: `${path.progress}%`,
                      backgroundColor: getDifficultyColor(path.difficulty)
                    }
                  ]} 
                />
              </View>
              <Text style={[styles.progressText, { color: colors.text }]}>
                {Math.round(path.progress)}%
              </Text>
            </View>

            <View style={styles.skillsContainer}>
              {path.skills.map((skill, index) => (
                <View key={index} style={[styles.skillTag, { backgroundColor: colors.text + '15' }]}>
                  <Text style={[styles.skillText, { color: colors.text }]}>{skill}</Text>
                </View>
              ))}
            </View>

            <View style={styles.pathFooter}>
              <View style={styles.timeContainer}>
                <Ionicons name="time-outline" size={16} color={colors.text + 'CC'} />
                <Text style={[styles.timeText, { color: colors.text + 'CC' }]}>
                  {path.estimatedTime}
                </Text>
              </View>
              
              <TouchableOpacity 
                style={[styles.startButton, { backgroundColor: getDifficultyColor(path.difficulty) }]}
                onPress={() => startLearningPath(path.id)}
              >
                <Text style={styles.startButtonText}>Começar</Text>
                <Ionicons name="arrow-forward" size={16} color="white" />
              </TouchableOpacity>
            </View>
          </View>
        </TouchableOpacity>
      ))}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  pathCard: {
    borderRadius: 16,
    marginBottom: 16,
    borderWidth: 2,
    overflow: 'hidden',
    elevation: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  gradientHeader: {
    height: 8,
  },
  recommendedBadge: {
    position: 'absolute',
    top: -4,
    right: 16,
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFD700',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 12,
  },
  recommendedText: {
    color: '#000',
    fontSize: 12,
    fontWeight: 'bold',
    marginLeft: 4,
  },
  pathContent: {
    padding: 16,
  },
  pathHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  pathTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    flex: 1,
  },
  difficultyBadge: {
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 16,
  },
  difficultyText: {
    color: 'white',
    fontSize: 12,
    fontWeight: 'bold',
    textTransform: 'uppercase',
  },
  pathDescription: {
    fontSize: 14,
    marginBottom: 16,
    lineHeight: 20,
  },
  progressContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  progressBar: {
    flex: 1,
    height: 8,
    backgroundColor: '#E0E0E0',
    borderRadius: 4,
    marginRight: 12,
  },
  progressFill: {
    height: '100%',
    borderRadius: 4,
  },
  progressText: {
    fontSize: 14,
    fontWeight: 'bold',
  },
  skillsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginBottom: 16,
  },
  skillTag: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
    marginRight: 8,
    marginBottom: 8,
  },
  skillText: {
    fontSize: 12,
    fontWeight: '500',
  },
  pathFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  timeContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  timeText: {
    fontSize: 14,
    marginLeft: 4,
  },
  startButton: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
  },
  startButtonText: {
    color: 'white',
    fontWeight: 'bold',
    marginRight: 4,
  },
});

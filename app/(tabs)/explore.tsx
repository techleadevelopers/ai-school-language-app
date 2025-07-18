
import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Alert, ScrollView, Dimensions, Text, TouchableOpacity } from 'react-native';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import { VoiceButton } from '@/components/VoiceButton';
import { FeedbackBox } from '@/components/FeedbackBox';
import { XPProgressBar } from '@/components/XPProgressBar';
import { AchievementSystem } from '@/components/AchievementSystem';
import { useThemeColor } from '@/hooks/useThemeColor';
import { analytics } from '@/service/analytics';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import bilingualAIApi, { AudioAnalysis, ChatMessage, ChatResponse } from '@/service/api';

const { width } = Dimensions.get('window');

type DifficultyLevel = 'beginner' | 'intermediate' | 'advanced';

interface ExtendedFeedback {
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

interface ChatInterface {
  messages: ChatMessage[];
  isTyping: boolean;
  contextualSuggestions: string[];
}

// Enhanced lesson phrases with more variety
const LESSON_PHRASES = {
  beginner: [
    "Hello, how are you?",
    "My name is Sarah.",
    "I am learning English.",
    "Thank you very much.",
    "Nice to meet you.",
    "Have a good day!",
    "See you later.",
    "Good morning.",
  ],
  intermediate: [
    "I would like to make a reservation.",
    "Could you please help me with this?",
    "I'm looking forward to meeting you.",
    "What do you think about this idea?",
    "I've been studying English for two years.",
    "That's a really interesting point.",
    "I'm not sure I understand what you mean.",
    "Let me think about it for a moment.",
  ],
  advanced: [
    "I believe this approach would be more effective in the long run.",
    "The implementation of this strategy requires careful consideration.",
    "Despite the challenges, I'm confident we can achieve our objectives.",
    "I'd like to discuss the implications of this decision.",
    "The correlation between these factors is quite significant.",
    "We need to analyze the data more thoroughly before proceeding.",
    "This phenomenon has been observed in various contexts.",
    "I appreciate your perspective on this complex issue.",
  ],
};

export default function ExploreScreen() {
  // State management
  const [currentPhrase, setCurrentPhrase] = useState('');
  const [currentDifficulty, setCurrentDifficulty] = useState<DifficultyLevel>('intermediate');
  const [feedback, setFeedback] = useState<ExtendedFeedback | null>(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [userXP, setUserXP] = useState(1250);
  const [userLevel, setUserLevel] = useState(8);
  const [streakDays, setStreakDays] = useState(12);
  const [isRecording, setIsRecording] = useState(false);
  const [chatInterface, setChatInterface] = useState<ChatInterface>({
    messages: [],
    isTyping: false,
    contextualSuggestions: [],
  });
  const [showChat, setShowChat] = useState(false);
  const [practiceMode, setPracticeMode] = useState<'pronunciation' | 'conversation' | 'lesson'>('pronunciation');
  const [dailyProgress, setDailyProgress] = useState(0);
  const [achievements, setAchievements] = useState<string[]>([]);

  // Theme colors
  const backgroundColor = useThemeColor({}, 'background');
  const textColor = useThemeColor({}, 'text');
  const tintColor = useThemeColor({}, 'tint');

  // Initialize component
  useEffect(() => {
    generatePhraseByDifficulty();
    loadUserProgress();
    initializeAIChatContext();
  }, []);

  useEffect(() => {
    generatePhraseByDifficulty();
  }, [currentDifficulty]);

  const generatePhraseByDifficulty = () => {
    const phrases = LESSON_PHRASES[currentDifficulty];
    const randomPhrase = phrases[Math.floor(Math.random() * phrases.length)];
    setCurrentPhrase(randomPhrase);
    setFeedback(null);
  };

  const loadUserProgress = async () => {
    try {
      // Load user progress from backend
      const progressResponse = await bilingualAIApi.getUserProgress('user123');
      if (progressResponse.success && progressResponse.data) {
        const progress = progressResponse.data;
        setUserXP(progress.fluency_score * 15); // Convert to XP
        setStreakDays(progress.consistency_streak);
        setDailyProgress(75); // Calculate from daily goals
      }

      // Load achievements
      const achievementsResponse = await bilingualAIApi.getUserAchievements('user123');
      if (achievementsResponse.success && achievementsResponse.data) {
        setAchievements(achievementsResponse.data.map((a: any) => a.name));
      }
    } catch (error) {
      console.error('Failed to load user progress:', error);
    }
  };

  const initializeAIChatContext = async () => {
    try {
      // Initialize AI chat with lesson context
      const topics = await bilingualAIApi.generateConversationTopics(
        ['pronunciation', 'daily_conversation'], 
        currentDifficulty
      );
      
      if (topics.success && topics.data) {
        setChatInterface(prev => ({
          ...prev,
          contextualSuggestions: topics.data.map((topic: any) => topic.title)
        }));
      }
    } catch (error) {
      console.error('Failed to initialize AI chat:', error);
    }
  };

  const changeDifficulty = (difficulty: DifficultyLevel) => {
    setCurrentDifficulty(difficulty);
    generatePhraseByDifficulty();
    // Update AI context
    initializeAIChatContext();
  };

  const analyzeAudioWithAdvancedAI = async (audioUri: string): Promise<ExtendedFeedback> => {
    try {
      setIsAnalyzing(true);
      
      // Send audio to advanced AI backend
      const analysisResponse = await bilingualAIApi.submitAudioForAnalysis(
        audioUri,
        currentPhrase,
        currentDifficulty,
        `${practiceMode}_practice`
      );

      if (analysisResponse.success && analysisResponse.data) {
        const analysis = analysisResponse.data;
        
        // Update user progress
        await updateUserProgress(analysis.overall_score);
        
        // Generate AI chat response based on performance
        await generateAIFeedbackChat(analysis);
        
        return {
          overall_score: analysis.overall_score,
          pronunciation_score: analysis.pronunciation_score,
          fluency_score: analysis.fluency_score,
          accuracy_score: analysis.accuracy_score,
          transcription: analysis.transcription,
          feedback: analysis.feedback,
          suggestions: analysis.suggestions || [],
          ai_insights: analysis.ai_insights || [],
          next_steps: analysis.next_steps || [],
          real_time_feedback: analysis.real_time_feedback || [],
          learning_insights: analysis.learning_insights || {
            learning_velocity: 'improving',
            strength_areas: ['pronunciation'],
            focus_areas: ['fluency'],
            recommended_practice: ['daily_practice'],
            next_milestone: 'advanced_level'
          },
          processing_time: analysis.processing_time || 0,
          model_confidence: analysis.model_confidence || 0.9
        };
      } else {
        throw new Error(analysisResponse.error || 'Analysis failed');
      }
    } catch (error) {
      console.error('Advanced AI analysis failed:', error);
      Alert.alert('Analysis Error', 'Failed to analyze audio. Please try again.');
      
      // Return fallback feedback
      return {
        overall_score: 0,
        pronunciation_score: 0,
        fluency_score: 0,
        accuracy_score: 0,
        transcription: '',
        feedback: 'Analysis failed. Please try again.',
        suggestions: ['Check your internet connection', 'Try again in a moment'],
        ai_insights: [],
        next_steps: [],
        real_time_feedback: [],
        learning_insights: {
          learning_velocity: 'stable',
          strength_areas: [],
          focus_areas: [],
          recommended_practice: [],
          next_milestone: ''
        },
        processing_time: 0,
        model_confidence: 0
      };
    } finally {
      setIsAnalyzing(false);
    }
  };

  const updateUserProgress = async (score: number) => {
    try {
      // Calculate XP gain
      const xpGain = Math.floor(score * 0.5) + 10;
      setUserXP(prev => prev + xpGain);
      
      // Update daily progress
      setDailyProgress(prev => Math.min(100, prev + 15));
      
      // Check for achievements
      if (score > 90) {
        setAchievements(prev => [...prev, 'Pronunciation Master']);
      }
      
      // Update streak
      await bilingualAIApi.updateUserStreak('user123');
      
    } catch (error) {
      console.error('Failed to update progress:', error);
    }
  };

  const generateAIFeedbackChat = async (analysis: any) => {
    try {
      const chatMessages: ChatMessage[] = [
        {
          role: 'user',
          content: `I just practiced: "${currentPhrase}". My score was ${analysis.overall_score}%.`,
          timestamp: new Date().toISOString()
        }
      ];

      const chatResponse = await bilingualAIApi.sendChatMessage(
        chatMessages,
        `pronunciation_practice_${currentDifficulty}`,
        'friendly_teacher'
      );

      if (chatResponse.success && chatResponse.data) {
        const aiMessage: ChatMessage = {
          role: 'assistant',
          content: chatResponse.data.response,
          timestamp: new Date().toISOString()
        };

        setChatInterface(prev => ({
          ...prev,
          messages: [...prev.messages, ...chatMessages, aiMessage],
          contextualSuggestions: chatResponse.data.follow_up_questions || []
        }));
      }
    } catch (error) {
      console.error('Failed to generate AI feedback chat:', error);
    }
  };

  const handleVoiceResult = async (audioUri: string) => {
    if (!audioUri) return;

    try {
      const analysisResult = await analyzeAudioWithAdvancedAI(audioUri);
      setFeedback(analysisResult);
      
      // Log analytics
      analytics.logEvent('audio_analyzed', {
        difficulty: currentDifficulty,
        score: analysisResult.overall_score,
        phrase: currentPhrase
      });
    } catch (error) {
      console.error('Voice analysis failed:', error);
    }
  };

  const handleChatMessage = async (message: string) => {
    try {
      setChatInterface(prev => ({
        ...prev,
        isTyping: true
      }));

      const userMessage: ChatMessage = {
        role: 'user',
        content: message,
        timestamp: new Date().toISOString()
      };

      const chatResponse = await bilingualAIApi.sendChatMessage(
        [...chatInterface.messages, userMessage],
        `${practiceMode}_context`,
        'friendly_teacher'
      );

      if (chatResponse.success && chatResponse.data) {
        const aiMessage: ChatMessage = {
          role: 'assistant',
          content: chatResponse.data.response,
          timestamp: new Date().toISOString()
        };

        setChatInterface(prev => ({
          ...prev,
          messages: [...prev.messages, userMessage, aiMessage],
          isTyping: false,
          contextualSuggestions: chatResponse.data.follow_up_questions || []
        }));
      }
    } catch (error) {
      console.error('Chat message failed:', error);
      setChatInterface(prev => ({
        ...prev,
        isTyping: false
      }));
    }
  };

  const renderPracticeModeSelector = () => (
    <View style={styles.practiceModeSelector}>
      <ThemedText type="subtitle" style={styles.sectionTitle}>
        🎯 Practice Mode
      </ThemedText>
      <View style={styles.modeButtons}>
        {(['pronunciation', 'conversation', 'lesson'] as const).map((mode) => (
          <TouchableOpacity
            key={mode}
            style={[
              styles.modeButton,
              practiceMode === mode && styles.activeModeButton
            ]}
            onPress={() => setPracticeMode(mode)}
          >
            <ThemedText style={[
              styles.modeButtonText,
              practiceMode === mode && styles.activeModeButtonText
            ]}>
              {mode.charAt(0).toUpperCase() + mode.slice(1)}
            </ThemedText>
          </TouchableOpacity>
        ))}
      </View>
    </View>
  );

  const renderDifficultySelector = () => (
    <View style={styles.difficultySelector}>
      <ThemedText type="subtitle" style={styles.sectionTitle}>
        📊 Difficulty Level
      </ThemedText>
      <View style={styles.difficultyButtons}>
        {(['beginner', 'intermediate', 'advanced'] as const).map((level) => (
          <TouchableOpacity
            key={level}
            style={[
              styles.difficultyButton,
              currentDifficulty === level && styles.activeDifficultyButton
            ]}
            onPress={() => changeDifficulty(level)}
          >
            <ThemedText style={[
              styles.difficultyButtonText,
              currentDifficulty === level && styles.activeDifficultyButtonText
            ]}>
              {level.charAt(0).toUpperCase() + level.slice(1)}
            </ThemedText>
          </TouchableOpacity>
        ))}
      </View>
    </View>
  );

  const renderProgressDashboard = () => (
    <View style={styles.progressDashboard}>
      <ThemedText type="subtitle" style={styles.sectionTitle}>
        📈 Your Progress
      </ThemedText>
      <View style={styles.progressStats}>
        <View style={styles.statCard}>
          <ThemedText style={styles.statValue}>{userXP}</ThemedText>
          <ThemedText style={styles.statLabel}>XP</ThemedText>
        </View>
        <View style={styles.statCard}>
          <ThemedText style={styles.statValue}>{streakDays}</ThemedText>
          <ThemedText style={styles.statLabel}>Day Streak</ThemedText>
        </View>
        <View style={styles.statCard}>
          <ThemedText style={styles.statValue}>{dailyProgress}%</ThemedText>
          <ThemedText style={styles.statLabel}>Daily Goal</ThemedText>
        </View>
      </View>
    </View>
  );

  const renderAIChatInterface = () => (
    <View style={styles.chatInterface}>
      <TouchableOpacity
        style={styles.chatToggle}
        onPress={() => setShowChat(!showChat)}
      >
        <Ionicons name="chatbubbles" size={24} color={tintColor} />
        <ThemedText style={styles.chatToggleText}>
          {showChat ? 'Hide' : 'Show'} AI Chat
        </ThemedText>
      </TouchableOpacity>
      
      {showChat && (
        <View style={styles.chatContainer}>
          <ScrollView style={styles.chatMessages}>
            {chatInterface.messages.map((message, index) => (
              <View key={index} style={[
                styles.messageContainer,
                message.role === 'user' ? styles.userMessage : styles.aiMessage
              ]}>
                <ThemedText style={styles.messageText}>
                  {message.content}
                </ThemedText>
              </View>
            ))}
            {chatInterface.isTyping && (
              <View style={[styles.messageContainer, styles.aiMessage]}>
                <ThemedText style={styles.messageText}>
                  🤖 AI is typing...
                </ThemedText>
              </View>
            )}
          </ScrollView>
          
          {chatInterface.contextualSuggestions.length > 0 && (
            <View style={styles.suggestions}>
              <ThemedText style={styles.suggestionsTitle}>Suggestions:</ThemedText>
              {chatInterface.contextualSuggestions.map((suggestion, index) => (
                <TouchableOpacity
                  key={index}
                  style={styles.suggestionButton}
                  onPress={() => handleChatMessage(suggestion)}
                >
                  <ThemedText style={styles.suggestionText}>
                    {suggestion}
                  </ThemedText>
                </TouchableOpacity>
              ))}
            </View>
          )}
        </View>
      )}
    </View>
  );

  return (
    <LinearGradient
      colors={['#667eea', '#764ba2']}
      style={styles.container}
    >
      <ScrollView showsVerticalScrollIndicator={false} style={styles.scrollView}>
        {/* Header */}
        <View style={styles.header}>
          <ThemedText type="title" style={styles.title}>
            🎤 Bilingui AI
          </ThemedText>
          <ThemedText type="subtitle" style={styles.subtitle}>
            Advanced AI Language Learning
          </ThemedText>
        </View>

        {/* Progress Dashboard */}
        {renderProgressDashboard()}

        {/* XP Progress Bar */}
        <XPProgressBar currentXP={userXP} level={userLevel} />

        {/* Achievement System */}
        <AchievementSystem 
          achievements={achievements} 
          streakDays={streakDays}
          onAchievementPress={(achievement) => {
            Alert.alert('Achievement', `You earned: ${achievement}! 🏆`);
          }}
        />

        {/* Practice Mode Selector */}
        {renderPracticeModeSelector()}

        {/* Difficulty Selector */}
        {renderDifficultySelector()}

        {/* Current Phrase */}
        <ThemedView style={styles.phraseContainer}>
          <ThemedText type="subtitle" style={styles.sectionTitle}>
            🗣️ Practice Phrase
          </ThemedText>
          <ThemedText style={styles.currentPhrase}>
            {currentPhrase}
          </ThemedText>
          <TouchableOpacity
            style={styles.regenerateButton}
            onPress={generatePhraseByDifficulty}
          >
            <Ionicons name="refresh" size={20} color={tintColor} />
            <ThemedText style={styles.regenerateText}>New Phrase</ThemedText>
          </TouchableOpacity>
        </ThemedView>

        {/* Voice Button */}
        <View style={styles.voiceButtonContainer}>
          <VoiceButton
            onResult={handleVoiceResult}
            isRecording={isRecording}
            setIsRecording={setIsRecording}
            targetPhrase={currentPhrase}
            difficulty={currentDifficulty}
          />
          {isAnalyzing && (
            <ThemedText style={styles.analyzingText}>
              🧠 AI is analyzing your pronunciation...
            </ThemedText>
          )}
        </View>

        {/* Feedback */}
        {feedback && (
          <FeedbackBox
            feedback={feedback}
            onTryAgain={generatePhraseByDifficulty}
            showAdvancedMetrics={true}
          />
        )}

        {/* AI Chat Interface */}
        {renderAIChatInterface()}
      </ScrollView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollView: {
    flex: 1,
    paddingHorizontal: 20,
  },
  header: {
    alignItems: 'center',
    marginTop: 50,
    marginBottom: 20,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FFFFFF',
    textAlign: 'center',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 18,
    color: '#FFFFFF',
    opacity: 0.9,
    textAlign: 'center',
  },
  progressDashboard: {
    marginBottom: 20,
  },
  progressStats: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 15,
    padding: 15,
    marginTop: 10,
  },
  statCard: {
    alignItems: 'center',
  },
  statValue: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  statLabel: {
    fontSize: 14,
    color: '#FFFFFF',
    opacity: 0.8,
    marginTop: 5,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#FFFFFF',
    marginBottom: 10,
  },
  practiceModeSelector: {
    marginBottom: 20,
  },
  modeButtons: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 15,
    padding: 5,
  },
  modeButton: {
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 10,
    flex: 1,
    alignItems: 'center',
    marginHorizontal: 2,
  },
  activeModeButton: {
    backgroundColor: '#FFFFFF',
  },
  modeButtonText: {
    fontSize: 14,
    color: '#FFFFFF',
    fontWeight: '500',
  },
  activeModeButtonText: {
    color: '#667eea',
  },
  difficultySelector: {
    marginBottom: 20,
  },
  difficultyButtons: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 15,
    padding: 5,
  },
  difficultyButton: {
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderRadius: 10,
    flex: 1,
    alignItems: 'center',
    marginHorizontal: 2,
  },
  activeDifficultyButton: {
    backgroundColor: '#FFFFFF',
  },
  difficultyButtonText: {
    fontSize: 14,
    color: '#FFFFFF',
    fontWeight: '500',
  },
  activeDifficultyButtonText: {
    color: '#667eea',
  },
  phraseContainer: {
    backgroundColor: 'rgba(255, 255, 255, 0.95)',
    borderRadius: 15,
    padding: 20,
    marginBottom: 20,
    alignItems: 'center',
  },
  currentPhrase: {
    fontSize: 20,
    fontWeight: '600',
    textAlign: 'center',
    marginBottom: 15,
    lineHeight: 28,
  },
  regenerateButton: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 8,
    paddingHorizontal: 16,
    backgroundColor: 'rgba(102, 126, 234, 0.1)',
    borderRadius: 20,
  },
  regenerateText: {
    marginLeft: 8,
    fontSize: 14,
    fontWeight: '500',
  },
  voiceButtonContainer: {
    alignItems: 'center',
    marginBottom: 20,
  },
  analyzingText: {
    marginTop: 15,
    fontSize: 16,
    color: '#FFFFFF',
    textAlign: 'center',
    fontStyle: 'italic',
  },
  chatInterface: {
    marginBottom: 20,
  },
  chatToggle: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 15,
    padding: 15,
    marginBottom: 10,
  },
  chatToggleText: {
    marginLeft: 10,
    fontSize: 16,
    color: '#FFFFFF',
    fontWeight: '500',
  },
  chatContainer: {
    backgroundColor: 'rgba(255, 255, 255, 0.95)',
    borderRadius: 15,
    padding: 15,
    maxHeight: 300,
  },
  chatMessages: {
    maxHeight: 200,
    marginBottom: 10,
  },
  messageContainer: {
    marginBottom: 10,
    padding: 10,
    borderRadius: 10,
    maxWidth: '80%',
  },
  userMessage: {
    alignSelf: 'flex-end',
    backgroundColor: '#667eea',
  },
  aiMessage: {
    alignSelf: 'flex-start',
    backgroundColor: '#f0f0f0',
  },
  messageText: {
    fontSize: 14,
    color: '#333333',
  },
  suggestions: {
    marginTop: 10,
  },
  suggestionsTitle: {
    fontSize: 14,
    fontWeight: '600',
    marginBottom: 8,
  },
  suggestionButton: {
    backgroundColor: '#f8f9fa',
    padding: 8,
    borderRadius: 8,
    marginBottom: 5,
  },
  suggestionText: {
    fontSize: 12,
    color: '#666666',
  },
});

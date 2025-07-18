
import React, { useState, useRef } from 'react';
import { TouchableOpacity, ActivityIndicator, StyleSheet, Alert, Animated } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useThemeColor } from '@/hooks/useThemeColor';
import { Audio } from 'expo-av';

interface VoiceButtonProps {
  onRecordingComplete?: (audioUri: string) => void;
  disabled?: boolean;
  currentPhrase?: string;
}

export const VoiceButton = ({ onRecordingComplete, disabled, currentPhrase }: VoiceButtonProps) => {
  const [isRecording, setIsRecording] = useState(false);
  const [recording, setRecording] = useState<Audio.Recording | null>(null);
  const [isProcessing, setIsProcessing] = useState(false);
  
  const color = useThemeColor({}, 'text');
  const primaryColor = useThemeColor({}, 'tint');
  const scaleAnim = useRef(new Animated.Value(1)).current;
  const pulseAnim = useRef(new Animated.Value(1)).current;

  React.useEffect(() => {
    if (isRecording) {
      // Pulse animation during recording
      Animated.loop(
        Animated.sequence([
          Animated.timing(pulseAnim, {
            toValue: 1.2,
            duration: 800,
            useNativeDriver: true,
          }),
          Animated.timing(pulseAnim, {
            toValue: 1,
            duration: 800,
            useNativeDriver: true,
          }),
        ])
      ).start();
    } else {
      pulseAnim.setValue(1);
    }
  }, [isRecording]);

  const startRecording = async () => {
    try {
      const permission = await Audio.requestPermissionsAsync();
      if (permission.status !== 'granted') {
        Alert.alert('Permissão Necessária', 'Precisamos de acesso ao microfone para funcionar.');
        return;
      }

      await Audio.setAudioModeAsync({
        allowsRecordingIOS: true,
        playsInSilentModeIOS: true,
      });

      const { recording } = await Audio.Recording.createAsync({
        android: {
          extension: '.m4a',
          outputFormat: Audio.RECORDING_OPTION_ANDROID_OUTPUT_FORMAT_MPEG_4,
          audioEncoder: Audio.RECORDING_OPTION_ANDROID_AUDIO_ENCODER_AAC,
          sampleRate: 44100,
          numberOfChannels: 2,
          bitRate: 128000,
        },
        ios: {
          extension: '.m4a',
          outputFormat: Audio.RECORDING_OPTION_IOS_OUTPUT_FORMAT_MPEG4AAC,
          audioQuality: Audio.RECORDING_OPTION_IOS_AUDIO_QUALITY_HIGH,
          sampleRate: 44100,
          numberOfChannels: 2,
          bitRate: 128000,
          linearPCMBitDepth: 16,
          linearPCMIsBigEndian: false,
          linearPCMIsFloat: false,
        },
        web: {
          mimeType: 'audio/webm',
          bitsPerSecond: 128000,
        },
      });

      setRecording(recording);
      setIsRecording(true);
      
      // Scale animation for button press
      Animated.spring(scaleAnim, {
        toValue: 0.95,
        useNativeDriver: true,
      }).start();
      
    } catch (err) {
      console.error('Failed to start recording', err);
      Alert.alert('Erro', 'Não foi possível iniciar a gravação.');
    }
  };

  const stopRecording = async () => {
    if (!recording) return;

    setIsRecording(false);
    setIsProcessing(true);
    
    // Reset animations
    Animated.spring(scaleAnim, {
      toValue: 1,
      useNativeDriver: true,
    }).start();

    try {
      await recording.stopAndUnloadAsync();
      const uri = recording.getURI();
      setRecording(null);
      
      if (uri && onRecordingComplete) {
        onRecordingComplete(uri);
      }
    } catch (error) {
      console.error('Failed to stop recording', error);
      Alert.alert('Erro', 'Erro ao finalizar gravação.');
    } finally {
      setIsProcessing(false);
    }
  };

  const handlePress = async () => {
    if (disabled) return;
    
    if (isRecording) {
      await stopRecording();
    } else {
      await startRecording();
    }
  };

  const getButtonStyle = () => {
    if (isProcessing) return [styles.button, styles.processing];
    if (isRecording) return [styles.button, styles.recording];
    return [styles.button, { backgroundColor: primaryColor }];
  };

  const getIconName = () => {
    if (isProcessing) return 'hourglass';
    if (isRecording) return 'stop';
    return 'mic';
  };

  return (
    <Animated.View style={{ transform: [{ scale: scaleAnim }, { scale: pulseAnim }] }}>
      <TouchableOpacity
        style={getButtonStyle()}
        onPress={handlePress}
        disabled={disabled || isProcessing}
        activeOpacity={0.8}
      >
        {isProcessing ? (
          <ActivityIndicator color="#fff" size={36} />
        ) : (
          <Ionicons name={getIconName()} size={36} color="#fff" />
        )}
      </TouchableOpacity>
    </Animated.View>
  );
};

const styles = StyleSheet.create({
  button: {
    marginVertical: 20,
    alignSelf: 'center',
    borderRadius: 50,
    padding: 20,
    elevation: 8,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    shadowColor: '#000',
  },
  recording: {
    backgroundColor: '#FF6B6B',
  },
  processing: {
    backgroundColor: '#4ECDC4',
  },
});

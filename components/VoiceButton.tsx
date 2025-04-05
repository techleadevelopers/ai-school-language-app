// 📁 components/VoiceButton.tsx
import React, { useState } from 'react';
import { TouchableOpacity, ActivityIndicator, StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useThemeColor } from '@/hooks/useThemeColor';

export const VoiceButton = () => {
  const [isRecording, setIsRecording] = useState(false);
  const color = useThemeColor({}, 'text');

  const handlePress = async () => {
    setIsRecording(!isRecording);
    // Lógica de gravação via API virá aqui (react-native-voice)
  };

  return (
    <TouchableOpacity style={styles.button} onPress={handlePress}>
      {isRecording ? (
        <ActivityIndicator color={color} />
      ) : (
        <Ionicons name="mic" size={36} color={color} />
      )}
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button: {
    marginVertical: 20,
    alignSelf: 'center',
    backgroundColor: '#66D2FF',
    borderRadius: 40,
    padding: 20,
  },
});
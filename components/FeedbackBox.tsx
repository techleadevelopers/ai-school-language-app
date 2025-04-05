import React from 'react';
import { View, StyleSheet } from 'react-native';
import Typography from './Typography';

const FeedbackBox = () => {
  const exampleFeedback = {
    corrigido: 'I went to the store yesterday.',
    explicacao: 'Use o verbo "go" no passado: "went".',
    novaFrase: 'Yesterday I went shopping.',
  };

  return (
    <View style={styles.box}>
      <Typography type="default">✅ Correção: {exampleFeedback.corrigido}</Typography>
      <Typography type="secondary">📘 Explicação: {exampleFeedback.explicacao}</Typography>
      <Typography type="link">💬 Frase alternativa: {exampleFeedback.novaFrase}</Typography>
    </View>
  );
};

const styles = StyleSheet.create({
  box: {
    backgroundColor: '#F0F4F8',
    borderRadius: 12,
    padding: 16,
    marginTop: 12,
  },
});

export default FeedbackBox;

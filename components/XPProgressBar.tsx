// 📁 components/XPProgressBar.tsx
import React from 'react';
import { View, StyleSheet } from 'react-native';
import  Typography  from './Typography';

interface Props {
  xp: number;
  level: number;
}

export const XPProgressBar = ({ xp, level }: Props) => {
  const progress = Math.min((xp % 100) / 100, 1);

  return (
    <View style={styles.container}>
      <Typography type="default">Nível {level} - XP: {xp}/100</Typography>
      <View style={styles.barBackground}>
        <View style={[styles.barFill, { width: `${progress * 100}%` }]} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginTop: 20,
  },
  barBackground: {
    height: 14,
    backgroundColor: '#D6E4F0',
    borderRadius: 7,
    marginTop: 4,
  },
  barFill: {
    height: 14,
    backgroundColor: '#66D2FF',
    borderRadius: 7,
  },
});

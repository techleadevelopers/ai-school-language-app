import React, { ReactNode } from 'react';
import { View, StyleSheet } from 'react-native';
import Colors from '../constants/Colors';
import { useColorScheme } from 'react-native';

type ContainerProps = {
  children: ReactNode;
};

const Container = ({ children }: ContainerProps) => {
  const colorScheme = useColorScheme() ?? 'light';
  const backgroundColor = Colors[colorScheme]?.background || '#FFFFFF';

  return <View style={[styles.container, { backgroundColor }]}>{children}</View>;
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
});

export default Container;

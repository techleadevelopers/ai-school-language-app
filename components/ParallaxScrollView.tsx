import React from 'react';
import { ScrollView, View, StyleSheet, useColorScheme } from 'react-native';

type Props = {
  children: React.ReactNode;
  headerBackgroundColor: { light: string; dark: string };
  headerImage?: React.ReactNode;
};

const ParallaxScrollView = ({ children, headerBackgroundColor, headerImage }: Props) => {
  const colorScheme = useColorScheme();
  const backgroundColor = headerBackgroundColor[colorScheme ?? 'light'];

  return (
    <ScrollView style={{ backgroundColor }}>
      <View style={styles.header}>{headerImage}</View>
      <View style={styles.body}>{children}</View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  header: {
    padding: 24,
  },
  body: {
    padding: 16,
  },
});

export default ParallaxScrollView;

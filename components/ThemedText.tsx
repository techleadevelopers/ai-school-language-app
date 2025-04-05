import React from 'react';
import { Text, StyleSheet, TextProps } from 'react-native';
import useColorScheme from '@/hooks/useColorScheme';
import Colors from '@/constants/Colors';

type TypographyType = 'title' | 'headline' | 'default' | 'secondary' | 'link';

interface ThemedTextProps extends TextProps {
  type?: TypographyType;
  children: React.ReactNode;
}

const ThemedText = ({ type = 'default', style, children, ...props }: ThemedTextProps) => {
  const colorScheme = useColorScheme();
  const themeColors = Colors[colorScheme];

  return (
    <Text
      style={[
        { color: themeColors.text },
        styles[type],
        style,
      ]}
      {...props}
    >
      {children}
    </Text>
  );
};

const styles = StyleSheet.create({
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 12,
  },
  headline: {
    fontSize: 22,
    fontWeight: '600',
    marginBottom: 8,
  },
  default: {
    fontSize: 16,
    lineHeight: 22,
  },
  secondary: {
    fontSize: 14,
    color: '#6B7280',
  },
  link: {
    fontSize: 16,
    color: '#2563EB',
    textDecorationLine: 'underline',
  },
});

export default ThemedText;

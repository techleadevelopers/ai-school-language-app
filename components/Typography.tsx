import React from 'react';
import { Text, TextStyle } from 'react-native';

type TypographyProps = {
  type?: 'title' | 'headline' | 'default' | 'secondary' | 'link';
  style?: TextStyle;
  children: React.ReactNode;
};

const Typography = ({ type = 'default', style, children }: TypographyProps) => {
  const getStyle = (): TextStyle => {
    switch (type) {
      case 'title':
        return { fontSize: 24, fontWeight: 'bold' };
      case 'headline':
        return { fontSize: 20, fontWeight: '600' };
      case 'secondary':
        return { color: '#6B7280' };
      case 'link':
        return { color: '#2563EB', textDecorationLine: 'underline' };
      default:
        return { fontSize: 16 };
    }
  };

  return <Text style={[getStyle(), style]}>{children}</Text>;
};

export default Typography;

// hooks/useColorScheme.ts
import { ColorSchemeName, useColorScheme as _useColorScheme } from 'react-native';

/**
 * Retorna o esquema de cores do sistema: 'light' | 'dark'
 */
export default function useColorScheme(): NonNullable<ColorSchemeName> {
  return _useColorScheme() ?? 'light';
}
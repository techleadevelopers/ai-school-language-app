// types/navigation.d.ts

declare module '@react-navigation/native' {
    import * as React from 'react';
  
    export interface NavigationContainerProps {
      children?: React.ReactNode;
      theme?: any;
    }
  
    export function NavigationContainer(props: NavigationContainerProps): JSX.Element;
  
    export function useNavigation(): any;
    export function useRoute(): any;
  
    export const ThemeProvider: React.ComponentType<any>;
  }
  
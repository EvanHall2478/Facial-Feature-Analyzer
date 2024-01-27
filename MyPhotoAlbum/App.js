import * as React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
// import Gallery from './screens/gallery';
// import Homepage from './screens/homepage';
// import Result from './screens/result';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Homepage"
          component={HomeScreen}
          options={{title: 'Welcome to My Photo Album'}}
        />
        <Stack.Screen
          name="Gallery"
          component={GalleryScreen}
        />
        <Stack.Screen
          name="Result"
          component={ResultScreen}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

const HomeScreen = ({navigation}) => {
  return (
    <View style={styles.container}>
      <Text>Welcome to My Photo Album</Text>
      <Button
        title="Go to Gallery"
        onPress={() => navigation.navigate('Gallery')}
      />
    </View>
  );
};

const GalleryScreen = ({navigation, route}) => {
  return (
    <View style={styles.container}>
      <Text>This is the Gallery Page</Text>
      <Button
        title="Go to Result"
        onPress={() => navigation.navigate('Result')}
      />
    </View>
  );
};

const ResultScreen = ({navigation, route}) => {
  return (
    <View style={styles.container}>
      <Text>This is the Result Page</Text>
      <Button title="Go back to Gallery" onPress={() => navigation.goBack()}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default App;

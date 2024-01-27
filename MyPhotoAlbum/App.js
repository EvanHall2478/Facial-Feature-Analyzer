import * as React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
// import Gallery from './screens/gallery';
// import Homepage from './screens/homrepage';
// import Result from './screens/result';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import * as ImagePicker from 'expo-image-picker';


const Stack = createNativeStackNavigator();

const App = () => {
  return (
    // This is where the main headers names for each page are declared
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Homepage"
          component={HomeScreen}
          options={{title: 'Photo Album'}}
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

// Asks the user for permission to access their photo library and redirects to the "GalleryScreen"
const HomeScreen = ({ navigation }) => {
  const handleButtonPress = async () => {
    // Ask for permission
    const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
    if (status !== 'granted') {
      alert('Sorry, we need camera roll permissions to make this work!');
      return;
    }

    // Open image picker
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      // allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
      allowsMultipleSelection: true,
    });
    console.log(!result.canceled)

    if (!result.canceled) {
      navigation.navigate('Gallery', { image: result.uri });
    } 

  };

  return (
    <View style={styles.container}>
      <Text>Project description</Text>
      <View style={styles.projectDescription}>
        <Button
          title="Get Started!"
          onPress={handleButtonPress}
        />
      </View>
    </View>
  );
};

const GalleryScreen = ({navigation, route}) => {
  return (
    <View style={styles.container}>
      <Text>This is the Gallery Page</Text>
      <View style={styles.projectDescription}>
        <Button
          title="Go to Result"
          onPress={() => navigation.navigate('Result')}
      />
      </View>
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

// Some basic styling for the app
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fdf6e4', // Warm, light beige background
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  projectDescription: {
    marginTop: 20,
    paddingHorizontal: 15,
    paddingVertical: 10,
    backgroundColor: '#b29a84', // Earthy tone for buttons and other elements
    borderRadius: 10,
  },
  text: {
    fontSize: 18,
    color: '#604d3f', // Darker, earthy tone for text
    textAlign: 'center',
    fontFamily: 'Cochin', // This font has a rustic feel; ensure it's available or choose a similar one
  },
  button: {
    backgroundColor: '#8c7b70', // Muted, earthy button color
    color: '#fff',
    padding: 10,
    borderRadius: 8,
    marginTop: 10,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
  },
});


export default App;

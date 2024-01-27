import * as React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
// import Gallery from './screens/gallery';
// import Homepage from './screens/homrepage';
// import Result from './screens/result';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import * as ImagePicker from 'expo-image-picker';

import {useAuth0, Auth0Provider} from 'react-native-auth0';

const Stack = createNativeStackNavigator();
const domain = "dev-vapqp1wmfekebndw.us.auth0.com";
const clientId = "BBttm33VHusqmAIQlWCcw8QVKKVrFtLe";

const App = () => {
  return (
    <Auth0Provider domain={domain} clientId={clientId}>
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen
            name="Home"
            component={HomeScreen}
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
    </Auth0Provider>
  );
};


// Asks the user for permission to access their photo library and redirects to the "GalleryScreen"
// TODO: How do I push the picuture images onto the KINTON database?
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

    if (!result.canceled) {
      navigation.navigate('Gallery', { image: result.uri });
    } 

  };

  const LoginButton = () => {
    const {authorize} = useAuth0();

    const onPress = async () => {
        try {
            await authorize();
        } catch (e) {
            console.log(e);
        }
    };

    return <Button onPress={onPress} title="Log in" />
  }

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
    //insert LoginButton here when done
  );
};

// This is where data from the kinton DB will be selectively displayed and pulled.
const GalleryScreen = ({navigation}) => {

  const LogoutButton = () => {
    const {clearSession} = useAuth0();

    const onPress = async () => {
        try {
            await clearSession();
        } catch (e) {
            console.log(e);
        }
    };

    return <Button onPress={onPress} title="Log out" />
  }

  return (
    <View style={styles.container}>
      <Text>This is the Gallery Page</Text>
      <View style={styles.projectDescription}>
        <Button
          title="Go to Result"
          onPress={() => navigation.navigate('Result')}
      />
      </View>
      <Button
        title="Logout"
        onPress={() => navigation.navigate('Home')}
      />
    </View>
    //insert LogoutButton here when done
  );
};

const ResultScreen = ({navigation}) => {
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

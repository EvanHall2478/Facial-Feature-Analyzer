import * as React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
// import Gallery from './screens/gallery';
// import Homepage from './screens/homepage';
// import Result from './screens/result';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
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


const HomeScreen = ({navigation}) => {
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
      <Text>Welcome to My Photo Album</Text>
      <Button
        title="Go to Gallery"
        onPress={() => navigation.navigate('Gallery')}
      />
    </View>
  );
};

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
      <Button
        title="Go to Result"
        onPress={() => navigation.navigate('Result')}
      />
      <Button
        title="Logout"
        onPress={() => navigation.navigate('Home')}
      />
    </View>
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

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default App;

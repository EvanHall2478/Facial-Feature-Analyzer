import React, { useState } from 'react';
import { StyleSheet, View } from 'react-native';
// import Gallery from './screens/gallery';
// import Homepage from './screens/homrepage';
// import Result from './screens/result';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import { Button, Text } from 'react-native-paper';
import { useEffect } from 'react';
import * as ImagePicker from 'expo-image-picker';

import {useAuth0, Auth0Provider} from 'react-native-auth0';
import { MultiSelect } from 'react-native-element-dropdown';
import AntDesign from '@expo/vector-icons/AntDesign';

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
    // const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
    // if (status !== 'granted') {
    //   alert('Sorry, we need camera roll permissions to make this work!');
    //   return;
    // }

    // Open image picker
    // const result = await ImagePicker.launchImageLibraryAsync({
    //   mediaTypes: ImagePicker.MediaTypeOptions.Images,
    //   // allowsEditing: true,
    //   aspect: [4, 3],
    //   quality: 1,
    //   allowsMultipleSelection: true,
    // });

    // if (!result.canceled) {
    navigation.navigate('Gallery');
    // } 

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

    return <Button mode="contained" onPress={onPress} title="Log in" />
  }

  return (
    <View style={styles.container}>
      <Text>"Welcome to an extraordinary journey, where the unexpected becomes the norm, and every turn unveils a new horizon of possibilities. As we embark on this adventure together, let's throw open the doors to imagination, let curiosity be our guide, and innovation our constant companion. In this realm, ideas dance freely, weaving a tapestry of creativity that stretches beyond the conventional. So, fasten your seatbelt and prepare for a delightful voyage through the uncharted territories of our collective minds, where each discovery is a celebration of the incredible tapestry of human thought and ingenuity."</Text>
      <View style={styles.projectDescription}>
      <Button 
        mode="contained"
        onPress={handleButtonPress}>
        Get Started!
      </Button>
      </View>
    </View>
    //insert LoginButton here when done
  );
};

const data = [
  { label: 'Item 1', value: '1' },
  { label: 'Item 2', value: '2' },
  { label: 'Item 3', value: '3' },
  { label: 'Item 4', value: '4' },
  { label: 'Item 5', value: '5' },
  { label: 'Item 6', value: '6' },
  { label: 'Item 7', value: '7' },
  { label: 'Item 8', value: '8' },
];

const MultiSelectComponent = () => {
  const [selected, setSelected] = useState([]);

  return (
      <MultiSelect
        style={styles.dropdown}
        placeholderStyle={styles.placeholderStyle}
        selectedTextStyle={styles.selectedTextStyle}
        inputSearchStyle={styles.inputSearchStyle}
        iconStyle={styles.iconStyle}
        search
        data={data}
        labelField="label"
        valueField="value"
        placeholder="Select item"
        searchPlaceholder="Search..."
        value={selected}
        onChange={item => {
          setSelected(item);
        }}
        renderLeftIcon={() => (
          <AntDesign
            style={styles.icon}
            color="black"
            name="Safety"
            size={20}
          />
        )}
        selectedStyle={styles.selectedStyle}
      />
  );
};

// This is where data from the kinton DB will be selectively displayed and pulled.
const GalleryScreen = ({  navigation  }) => {
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
      aspect: [4, 3],
      quality: 1,
      allowsMultipleSelection: true,
    });

    if (!result.canceled) {
      navigation.navigate('Gallery', { image: result.uri });
    }
    console.log(result)
  };

  useEffect(() => {
    handleButtonPress();
  }, []);


  const LogoutButton = () => {
    const { clearSession } = useAuth0();

    const onPress = async () => {
      try {
        await clearSession();
      } catch (e) {
        console.log(e);
      }
    };

    return <Button onPress={onPress} title="Log out" />;
  };
  
  return (
    <View style={styles.container}>
      <Text>This is the Gallery Page</Text>
      <MultiSelectComponent />
      <View style={styles.projectDescription}>
        <Button mode="contained" onPress={() => navigation.navigate('Result')}>
          Go to Result
        </Button>
      </View>
      <Button
        title="Logout"
        onPress={() => navigation.navigate('Home')}
        mode="contained"
        buttonColor="maroon"
      >
        Logout
      </Button>
    </View>
  );
};

const ResultScreen = ({navigation}) => {
  return (
    <View style={styles.container}>
      <Text>This is the Result Page</Text>
      <Button 
        // title="Go back to Gallery"
         onPress={() => navigation.goBack()}
         mode='contained'>
        Go back to Gallery
        </Button>
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
  dropdown: {
    height: 50,
    backgroundColor: 'transparent',
    borderBottomColor: 'gray',
    borderBottomWidth: 0.5,
  },
  projectDescription: {
    marginTop: 20,
    paddingHorizontal: 15,
    paddingVertical: 10,
    // backgroundColor: '#b29a84', // Earthy tone for buttons and other elements
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
  placeholderStyle: {
    fontSize: 16,
  },
  selectedTextStyle: {
    fontSize: 14,
  },
  iconStyle: {
    width: 20,
    height: 20,
  },
  inputSearchStyle: {
    height: 40,
    fontSize: 16,
  },
  icon: {
    marginRight: 5,
  },
  selectedStyle: {
    borderRadius: 12,
  },
});


export default App;

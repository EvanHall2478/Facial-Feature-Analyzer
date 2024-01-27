import React from 'react';
import { View, Text, Button } from 'react-native';

const Homepage = () => {
    return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
            <Text>Welcome to My Photo Album</Text>
            <Text> This is the description of the app</Text>
            <Button>Get Started!</Button>
        </View>
    );
};

export default Homepage;

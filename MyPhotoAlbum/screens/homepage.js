import React from 'react';
import { View, Text, Button } from 'react-native';

const Homepage = () => {
    return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
            <Text>Welcome to My Photo Album</Text>
            <Button title="Get Started" onPress={() => console.log('Button pressed!')} />
        </View>
    );
};

export default Homepage;

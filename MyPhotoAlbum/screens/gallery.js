import React from 'react';
import { View, Button } from 'react-native';

const Gallery = ({ navigation }) => {
    const redirectToResultPage = () => {
        navigation.navigate('Result');
    };

    return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
            <Button title="Go to Result Page" onPress={redirectToResultPage} />
        </View>
    );
};

export default Gallery;

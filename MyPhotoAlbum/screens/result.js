// Import the necessary modules
import React from 'react';
import { View, Button } from 'react-native';

// Define the ResultScreen component
const Result = ({ navigation }) => {
    // Function to navigate back to the gallery page
    const goBackToGallery = () => {
        navigation.navigate('Gallery');
    };

    return (
        <View>
            {/* Button to go back to the gallery page */}
            <Button title="Go Back to Gallery" onPress={goBackToGallery} />
        </View>
    );
};

export default Result;

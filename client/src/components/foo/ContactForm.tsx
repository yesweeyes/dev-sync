import React, {useState} from 'react';
import { View, TextInput, Button, Alert } from 'react-native';
import axios from 'axios';

function ContactForm() {
    const TEST_API_ENDPOINT = 'http://localhost:8000/api/foo'; // POST
    
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });

    const handleFormChange = (key: string, value: string) => {
        setFormData({
            ...formData,
            [key]: value
        });
    }

    const handleFormSubmit = async () => {
        try {
            await axios.post(TEST_API_ENDPOINT, formData);
            Alert.alert('Message sent!');
        } catch (error) {
            Alert.alert('Failed to send message');
        }
    }


    return (
    <View>
        <TextInput
            placeholder="Name"
            onChangeText={(text) => handleFormChange('name', text)}
        />

        <TextInput
            placeholder="Email"
            onChangeText={(text) => handleFormChange('email', text)}
        />

        <TextInput
            placeholder="Message"
            onChangeText={(text) => handleFormChange('message', text)}
        />

        <Button
            title="Submit"
            onPress={handleFormSubmit}
        />
    </View>
    );
};

export default ContactForm;
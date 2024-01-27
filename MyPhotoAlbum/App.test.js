import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import HomeScreen from './screens/homepage';

describe('HomeScreen', () => {
  test('renders project description', () => {
    const { getByText } = render(<HomeScreen />);
    const projectDescription = getByText('Project description');
    expect(projectDescription).toBeTruthy();
  });

  test('navigates to GalleryScreen on button press when permission is granted', async () => {
    const navigationMock = { navigate: jest.fn() };
    const { getByText } = render(<HomeScreen navigation={navigationMock} />);
    const button = getByText('Get Started!');
    fireEvent.press(button);
    expect(navigationMock.navigate).toHaveBeenCalledWith('Gallery');
  });

  test('requests permission and navigates to GalleryScreen on button press when permission is denied and then granted', async () => {
    const checkMock = jest.fn().mockResolvedValue('denied');
    const requestMock = jest.fn().mockResolvedValue('granted');
    const navigationMock = { navigate: jest.fn() };
    jest.mock('react-native-permissions', () => ({
      check: checkMock,
      request: requestMock,
    }));

    const { getByText } = render(<HomeScreen navigation={navigationMock} />);
    const button = getByText('Get Started!');
    fireEvent.press(button);
    expect(checkMock).toHaveBeenCalledWith('photo-library');
    expect(requestMock).toHaveBeenCalledWith('photo-library');
    expect(navigationMock.navigate).toHaveBeenCalledWith('Gallery');
  });

  test('logs error when permission check fails', async () => {
    const checkMock = jest.fn().mockRejectedValue(new Error('Permission check failed'));
    const consoleWarnMock = jest.spyOn(console, 'warn').mockImplementation(() => {});
    jest.mock('react-native-permissions', () => ({
      check: checkMock,
    }));

    const { getByText } = render(<HomeScreen />);
    const button = getByText('Get Started!');
    fireEvent.press(button);
    expect(checkMock).toHaveBeenCalledWith('photo-library');
    expect(consoleWarnMock).toHaveBeenCalledWith(new Error('Permission check failed'));
  });
});
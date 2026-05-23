class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+ 273.15,celsius*1.80+32.00]
        #Logic: To convert the temperature from Celsius to Kelvin, we can add 273.15 to the Celsius temperature. To convert the temperature from Celsius to Fahrenheit, we can multiply the Celsius temperature by 1.80 and then add 32.00.
        #time complexity: O(1) since we are performing a constant number of operations to convert the temperature.
        #space complexity: O(1) since we are not using any extra space, we are just returning a list of two elements.
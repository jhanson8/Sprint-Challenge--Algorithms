class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    #Bubble Sort 
    #We must initially set the light to off to indicate the list is not sorted 
    #While the list is not sorted, we will turn the light on and assume the list is sorted 
    #While we are able to move right on the list 
    #Use the compare function to look at the cur number and the one ahead 
        #if the cur number is greater than the one ahead (retruns 1)
            #use swap function to swap number 
            #set light to off because list is not sorted 
            #move right 
        #if cur number is less than the one ahead 
            #move right 
    #Start from begining index and run the while loop until sorted 
        

    #Space is O(1) b/c we do all of the sorting in place of same array 
    #Time O(n) b/c we will loop through until sorted 
    def sort(self):
        """
        Sort the robot's list.
        """
        #Fill this out
        #We must first set the light to off. Equivalent to saying the list is not sorted.
        self.set_light_off()
        #While the list is not sorted we will tentatively assume that is is on this iteration. 
        while not self.light_is_on() == True:
            self.set_light_on()
            #15, 41, 58, 49
            #None, 41, 48, 49 
            #move to index 2
            #Compare item 15 with index 2 item 
            #its less than so move back to index 1 
            #swap back 15 for None 
            #move right 
            #While our pointer can move right on our list, 
            while self.can_move_right() == True:
                #None is considered an item 
                #when we swap the current position is changed to None value and assigns value to item. Like take item 
                self.swap_item()
                #move position to right one index 
                self.move_right()
                #if self._item is greater than the position item we are at 
                if self.compare_item() == 1:
                    self.swap_item() 
                    self.set_light_off
                    
                #always need to move back an index to swap out the None with our item 
                self.move_left()
                self.swap_item()
                self.move_right()

            #if we hit this while loop and move left, we are at the end of the list 
            #15, 41, 58, 49
            #15, 41, 49, 58
            while self.can_move_left() == True:
                self.swap_item() #take item 
                self.move_left() #move index over to left one 

                #if the cur held item value is less than the one we are at 
                if self.compare_item() == -1:
                    self.swap_item()
                    self.set_light_off()
            
                self.move_right()
                self.swap_item()
                self.move_left()
            
            

                #elif self.compare_item() == -1:
                    #self.move_right()
                #elif self.compare_item() == 0:
                    #self.move_right()
            

        #return self.light_is_on()



     
    
    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"
    



   

        


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
   
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
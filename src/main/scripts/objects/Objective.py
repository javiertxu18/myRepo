from multipledispatch import dispatch


class Objective:
    # Constructor
    def __init__(self):
        self._target = ""
        self._shadow = ""

    # Getters & Setters
    # Sets the target
    @dispatch(str)
    def _setTarget(self, newTarget):
        self._target = newTarget
        self._setShadow()

    # Gets the target
    def getTarget(self):
        return self._target

    # Sets the shadow (_target covered with asterisks)
    def _setShadow(self):
        for x in self._target:
            if x != " ":
                self._shadow += "*"
            else:
                self._shadow += " "

    # Gets the shadow
    def getShadow(self):
        return self._shadow

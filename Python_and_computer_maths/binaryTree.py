class BinaryNode:
    """Буферный класс для создания поддерева в дереве

    Argumnets:
    
    left: левое поддерево

    value: значение

    right: правое поддерево
    """

    def __init__(self, left, value, right):
        self.left = left
        self.value = value
        self.right = right

    def lcr(self):
        """Отсортированный список значений из узлов дерева
        
        Arguments: None

        Returns: Остортированный список
        """
        return self.left.lcr() + [self.value] + self.right.lcr()

    def max(self):
        """Максимальное значение из узлов дерева

        Arguments: None

        Returns: число соответствующее максимальному значению в дереве        
        """
        return self.right.max() if isinstance(self.right, BinaryNode) else self.value

    def min(self):
        """Минимальное значение из узлов дерева

        Arguments: None

        Returns: число соответствующее минимальному значению в дереве
        """
        return self.left.min() if isinstance(self.left, BinaryNode) else self.value

    def __repr__(self):
        return f'({self.left}, {self.value}, {self.right})'

    def insert(self, value):
        """Вставка элемента в дерево

        Arguments:

        value: значение для вставки

        Returns: None        
        """
        if value < self.value:
            self.left = self.left.insert(value)
        else:
            self.right = self.right.insert(value)
        return self
    
    def __contains__(self, value):
        return (value in self.left) or value == self.value or (value in self.right)
    
    def __len__(self):
        return len(self.left) + len(self.right) + 1
    
class EmptyNode:
    """Заглушка для BinaryNode    
    """

    def __repr__(self):
        return '*'
    
    def min(self):
        """Минимальное значение из узлов дерева

        Arguments: None

        Returns: nothing
        """
        return None
    
    def max(self):
        """Максимальное значение из узлов дерева

        Arguments: None

        Returns: nothing
        """
        return None
    
    def lcr(self):
        """Отсортированный список значений из узлов дерева
        
        Arguments: None

        Returns: пустой список
        """
        return []

    def insert(self, value):
        return BinaryNode(self, value, self)

    def __contains__(self, value):
        return False
    
    def __len__(self):
        return 0
    
class BinaryTree:
    """Бинарное дерево поиска

    Methods:

    min: минимальное значение в дереве

    max: максимальное значение в дереве

    lcr: значения элементов дерева в отсортированном списке    
    """
    def __init__(self):
        self.root = EmptyNode()

    def min(self):
        """Минимальное значение из узлов дерева

        Arguments: None

        Returns: число соответствующее минимальному значению в дереве        
        """
        return self.root.min()
    
    def max(self):
        """Максимальное значение из узлов дерева

        Arguments: None

        Returns: число соответствующее максимальному значению в дереве        
        """
        return self.root.max()

    def lcr(self):
        """Отсортированный список значений из узлов дерева
        
        Arguments: None

        Returns: Остортированный список
        """
        return self.root.lcr()

    def __repr__(self):
        return repr(self.root)

    def insert(self, value):
        """Вставка элемента в дерево
        
        Argumentsa:
        
        value: значение для вставки

        Returns: None
        """
        self.root = self.root.insert(value) 
    
    def __contains__(self, value):
        return value in self.root
    
    def __len__(self):
        return len(self.root)
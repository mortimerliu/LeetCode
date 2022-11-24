class ListNode:
    """
    A generalized class representing a node in Double Linked Lists.

    Can also be used in Single Linked Lists, just ignore the `prev`
    attribute.

    Additional attributes can be specified by keyword arguments in
    `__init__`.
    """

    def __init__(self, val=0, prev=None, next=None, **kwargs):
        self.val = val
        self.prev = prev
        self.next = next
        for k, v in kwargs.items():
            setattr(self, k, v)

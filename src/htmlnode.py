class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")

    def props_to_html(self):
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return (f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
                f"children={self.children!r}, props={self.props!r})")

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value 
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        if tag is None:
            raise ValueError("A tag must be provided for ParentNode")
        if children is None:
            raise ValueError("Children cannot be None for ParentNode")
        if not isinstance(children, list):
            raise TypeError("Children must be provided as a list")
        super().__init__(tag)
        self.children = children

    def to_html(self):
        if not self.children:
            raise TypeError("ParentNode must have at least one child")

        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}>{children_html}</{self.tag}>"

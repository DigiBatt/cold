
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PropertyModule import Property



from .DeclaredModule import Declared





from .MetrologicalReferenceModule import MetrologicalReference





class Quantity(Property, Declared):
    """
    Class representing the `Quantity` entity, which inherits from:
    - Property, Declared

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0650c031_42b6_4f0a_b62d_d88f071da6bf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Quantity'`
        - **Alias**: `class_name`
    
    - `hasMetrologicalReference` (`Optional[MetrologicalReference]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMetrologicalReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Quantity(
    
    class_iri='https://w3id.org/emmo#EMMO_0650c031_42b6_4f0a_b62d_d88f071da6bf',
    
    class_name='Quantity',
    
    hasMetrologicalReference="example_value",
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    VIMTerm="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0650c031_42b6_4f0a_b62d_d88f071da6bf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Quantity',
        alias="class_name"
    )
    
    hasMetrologicalReference: Optional[MetrologicalReference] = Field(
        None,
        alias="hasMetrologicalReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    @validator("hasMetrologicalReference", pre=True, always=True)
    def validate_hasMetrologicalReference(cls, value):
        if value is not None and not isinstance(value, MetrologicalReference):
            raise ValueError(f"Field 'hasMetrologicalReference' must be an instance of 'MetrologicalReference' or its subclass.")
        return value
    
    

    

    
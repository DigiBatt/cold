
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeclaredModule import Declared





from .PropertyModule import Property





class CharacterisationEnvironment(Declared):
    """
    Class representing the `CharacterisationEnvironment` entity, which inherits from:
    - Declared

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationEnvironment'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationEnvironment'`
        - **Alias**: `class_name`
    
    - `hasProperty` (`Optional[Property]`): 
        - **Default Value**: `None`
        - **Alias**: `hasProperty`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationEnvironment(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationEnvironment',
    
    class_name='CharacterisationEnvironment',
    
    hasProperty="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationEnvironment',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationEnvironment',
        alias="class_name"
    )
    
    hasProperty: Optional[Property] = Field(
        None,
        alias="hasProperty"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    @validator("hasProperty", pre=True, always=True)
    def validate_hasProperty(cls, value):
        if value is not None and not isinstance(value, Property):
            raise ValueError(f"Field 'hasProperty' must be an instance of 'Property' or its subclass.")
        return value
    
    

    

    
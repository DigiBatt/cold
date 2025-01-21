
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DigitalDataModule import DigitalData



from .SystemResourceModule import SystemResource



from .DeclaredModule import Declared





from .ResourceIdentifierModule import ResourceIdentifier





class File(DigitalData, SystemResource, Declared):
    """
    Class representing the `File` entity, which inherits from:
    - DigitalData, SystemResource, Declared

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_998dd3a0_c85f_4c8d_9fb8_816a93cc3bb8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'File'`
        - **Alias**: `class_name`
    
    - `hasResourceIdentifier` (`Optional[ResourceIdentifier]`): 
        - **Default Value**: `None`
        - **Alias**: `hasResourceIdentifier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = File(
    
    class_iri='https://w3id.org/emmo#EMMO_998dd3a0_c85f_4c8d_9fb8_816a93cc3bb8',
    
    class_name='File',
    
    hasResourceIdentifier="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_998dd3a0_c85f_4c8d_9fb8_816a93cc3bb8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'File',
        alias="class_name"
    )
    
    hasResourceIdentifier: Optional[ResourceIdentifier] = Field(
        None,
        alias="hasResourceIdentifier"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasResourceIdentifier", pre=True, always=True)
    def validate_hasResourceIdentifier(cls, value):
        if value is not None and not isinstance(value, ResourceIdentifier):
            raise ValueError(f"Field 'hasResourceIdentifier' must be an instance of 'ResourceIdentifier' or its subclass.")
        return value
    
    

    

    
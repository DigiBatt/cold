
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MassModule import Mass







class AtomicMass(Mass):
    """
    Class representing the `AtomicMass` entity, which inherits from:
    - Mass

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_27367073_ed8a_481a_9b07_f836dfe31f7f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AtomicMass'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AtomicMass(
    
    class_iri='https://w3id.org/emmo#EMMO_27367073_ed8a_481a_9b07_f836dfe31f7f',
    
    class_name='AtomicMass',
    
    iupacReference="example_value",
    
    definition="example_value",
    
    ISO80000Reference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_27367073_ed8a_481a_9b07_f836dfe31f7f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AtomicMass',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ForceModule import Force



from .MechanicalQuantityModule import MechanicalQuantity







class StaticFrictionForce(Force, MechanicalQuantity):
    """
    Class representing the `StaticFrictionForce` entity, which inherits from:
    - Force, MechanicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_445d186f_1896_4752_8940_384f98440cfe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StaticFrictionForce'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StaticFrictionForce(
    
    class_iri='https://w3id.org/emmo#EMMO_445d186f_1896_4752_8940_384f98440cfe',
    
    class_name='StaticFrictionForce',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_445d186f_1896_4752_8940_384f98440cfe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StaticFrictionForce',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    
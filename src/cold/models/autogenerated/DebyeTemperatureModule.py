
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermodynamicTemperatureModule import ThermodynamicTemperature



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity







class DebyeTemperature(ThermodynamicTemperature, CondensedMatterPhysicsQuantity):
    """
    Class representing the `DebyeTemperature` entity, which inherits from:
    - ThermodynamicTemperature, CondensedMatterPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_74cfc811_6e04_4fe4_aea5_6a5cc09f6571'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DebyeTemperature'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DebyeTemperature(
    
    class_iri='https://w3id.org/emmo#EMMO_74cfc811_6e04_4fe4_aea5_6a5cc09f6571',
    
    class_name='DebyeTemperature',
    
    wikidataReference="example_value",
    
    qudtReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_74cfc811_6e04_4fe4_aea5_6a5cc09f6571',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DebyeTemperature',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    
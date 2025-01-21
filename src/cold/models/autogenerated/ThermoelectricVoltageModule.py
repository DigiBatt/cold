
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VoltageModule import Voltage



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity







class ThermoelectricVoltage(Voltage, CondensedMatterPhysicsQuantity):
    """
    Class representing the `ThermoelectricVoltage` entity, which inherits from:
    - Voltage, CondensedMatterPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fec651dc_8962_48c3_8b30_1115b2dd7c16'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermoelectricVoltage'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermoelectricVoltage(
    
    class_iri='https://w3id.org/emmo#EMMO_fec651dc_8962_48c3_8b30_1115b2dd7c16',
    
    class_name='ThermoelectricVoltage',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fec651dc_8962_48c3_8b30_1115b2dd7c16',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermoelectricVoltage',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    
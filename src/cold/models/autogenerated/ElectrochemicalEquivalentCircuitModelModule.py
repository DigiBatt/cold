
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectronicModelModule import ElectronicModel







class ElectrochemicalEquivalentCircuitModel(ElectronicModel):
    """
    Class representing the `ElectrochemicalEquivalentCircuitModel` entity, which inherits from:
    - ElectronicModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_679f6984_e0dc_4285_9dbb_429c5779590c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalEquivalentCircuitModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalEquivalentCircuitModel(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_679f6984_e0dc_4285_9dbb_429c5779590c',
    
    class_name='ElectrochemicalEquivalentCircuitModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_679f6984_e0dc_4285_9dbb_429c5779590c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalEquivalentCircuitModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
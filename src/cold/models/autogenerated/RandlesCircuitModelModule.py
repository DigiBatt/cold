
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalEquivalentCircuitModelModule import ElectrochemicalEquivalentCircuitModel







class RandlesCircuitModel(ElectrochemicalEquivalentCircuitModel):
    """
    Class representing the `RandlesCircuitModel` entity, which inherits from:
    - ElectrochemicalEquivalentCircuitModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_e939a312_661c_4b21_9651_06f34659e20a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RandlesCircuitModel'`
        - **Alias**: `class_name`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RandlesCircuitModel(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_e939a312_661c_4b21_9651_06f34659e20a',
    
    class_name='RandlesCircuitModel',
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_e939a312_661c_4b21_9651_06f34659e20a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RandlesCircuitModel',
        alias="class_name"
    )
    
    dbpediaReference: Optional[str] = Field(
        None,
        alias="dbpediaReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricConductivityModule import ElectricConductivity



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class ElectronicConductivity(ElectricConductivity, ElectrochemicalQuantity):
    """
    Class representing the `ElectronicConductivity` entity, which inherits from:
    - ElectricConductivity, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ce74d2dc_d496_4116_b2fb_3e83d88bc744'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectronicConductivity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectronicConductivity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ce74d2dc_d496_4116_b2fb_3e83d88bc744',
    
    class_name='ElectronicConductivity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ce74d2dc_d496_4116_b2fb_3e83d88bc744',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectronicConductivity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
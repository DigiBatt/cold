
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DensityModule import Density



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class CalenderedDensity(Density, ElectrochemicalQuantity):
    """
    Class representing the `CalenderedDensity` entity, which inherits from:
    - Density, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_520995f8_ec9c_4b3c_bb64_2cd691947379'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalenderedDensity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalenderedDensity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_520995f8_ec9c_4b3c_bb64_2cd691947379',
    
    class_name='CalenderedDensity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_520995f8_ec9c_4b3c_bb64_2cd691947379',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalenderedDensity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
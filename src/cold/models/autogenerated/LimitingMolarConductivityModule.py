
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MolarConductivityModule import MolarConductivity



from .ElectrochemicalTransportQuantityModule import ElectrochemicalTransportQuantity







class LimitingMolarConductivity(MolarConductivity, ElectrochemicalTransportQuantity):
    """
    Class representing the `LimitingMolarConductivity` entity, which inherits from:
    - MolarConductivity, ElectrochemicalTransportQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a17ee4e0_c81a_4a64_9ecb_9c6fa022cf4d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LimitingMolarConductivity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LimitingMolarConductivity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a17ee4e0_c81a_4a64_9ecb_9c6fa022cf4d',
    
    class_name='LimitingMolarConductivity',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a17ee4e0_c81a_4a64_9ecb_9c6fa022cf4d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LimitingMolarConductivity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    
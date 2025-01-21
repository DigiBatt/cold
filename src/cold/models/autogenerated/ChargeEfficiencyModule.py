
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class ChargeEfficiency(RatioQuantity, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `ChargeEfficiency` entity, which inherits from:
    - RatioQuantity, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a5962e05_466d_46a4_8951_bea59d7326e5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargeEfficiency'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargeEfficiency(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a5962e05_466d_46a4_8951_bea59d7326e5',
    
    class_name='ChargeEfficiency',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a5962e05_466d_46a4_8951_bea59d7326e5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargeEfficiency',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
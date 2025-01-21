
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class AreicCapacity(ISQDerivedQuantity, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `AreicCapacity` entity, which inherits from:
    - ISQDerivedQuantity, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bcb33f7e_5573_4bc2_b636_4ea313a9dd3a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AreicCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AreicCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bcb33f7e_5573_4bc2_b636_4ea313a9dd3a',
    
    class_name='AreicCapacity',
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bcb33f7e_5573_4bc2_b636_4ea313a9dd3a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AreicCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    
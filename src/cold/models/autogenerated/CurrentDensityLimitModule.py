
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentDensityModule import ElectricCurrentDensity



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class CurrentDensityLimit(ElectricCurrentDensity, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `CurrentDensityLimit` entity, which inherits from:
    - ElectricCurrentDensity, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_76e7e556_f47e_47e2_b2ef_67aeed09c63e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CurrentDensityLimit'`
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
    obj = CurrentDensityLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_76e7e556_f47e_47e2_b2ef_67aeed09c63e',
    
    class_name='CurrentDensityLimit',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_76e7e556_f47e_47e2_b2ef_67aeed09c63e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CurrentDensityLimit',
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
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class EnergyEfficiency(RatioQuantity, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `EnergyEfficiency` entity, which inherits from:
    - RatioQuantity, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79198264_cdf5_4fc3_8bcf_e5140a52547a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EnergyEfficiency'`
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
    obj = EnergyEfficiency(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79198264_cdf5_4fc3_8bcf_e5140a52547a',
    
    class_name='EnergyEfficiency',
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79198264_cdf5_4fc3_8bcf_e5140a52547a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EnergyEfficiency',
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
    

    
    

    

    
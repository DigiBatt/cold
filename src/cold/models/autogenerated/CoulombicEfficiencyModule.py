
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class CoulombicEfficiency(RatioQuantity, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `CoulombicEfficiency` entity, which inherits from:
    - RatioQuantity, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5696453c_9da7_41e2_bbda_603c1b90a8fc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CoulombicEfficiency'`
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
    obj = CoulombicEfficiency(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5696453c_9da7_41e2_bbda_603c1b90a8fc',
    
    class_name='CoulombicEfficiency',
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5696453c_9da7_41e2_bbda_603c1b90a8fc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CoulombicEfficiency',
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
    

    
    

    

    
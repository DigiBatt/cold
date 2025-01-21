
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalModule import Electrochemical



from .ElectrochemicalTestingProcedureModule import ElectrochemicalTestingProcedure







class ReferencePerformanceTest(Electrochemical, ElectrochemicalTestingProcedure):
    """
    Class representing the `ReferencePerformanceTest` entity, which inherits from:
    - Electrochemical, ElectrochemicalTestingProcedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c7e37e88_ed86_4acd_99ee_b6a2a5fcbd24'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReferencePerformanceTest'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ReferencePerformanceTest(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c7e37e88_ed86_4acd_99ee_b6a2a5fcbd24',
    
    class_name='ReferencePerformanceTest',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c7e37e88_ed86_4acd_99ee_b6a2a5fcbd24',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReferencePerformanceTest',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
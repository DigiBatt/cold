
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkflowModule import Workflow



from .ProcedureModule import Procedure







class ElectrochemicalTestingProcedure(Workflow, Procedure):
    """
    Class representing the `ElectrochemicalTestingProcedure` entity, which inherits from:
    - Workflow, Procedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_830d02dd_f897_4c3c_95a7_c5e5eafa346a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalTestingProcedure'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalTestingProcedure(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_830d02dd_f897_4c3c_95a7_c5e5eafa346a',
    
    class_name='ElectrochemicalTestingProcedure',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_830d02dd_f897_4c3c_95a7_c5e5eafa346a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalTestingProcedure',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
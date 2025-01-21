
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConcentrationLimitModule import ConcentrationLimit







class MaximumConcentration(ConcentrationLimit):
    """
    Class representing the `MaximumConcentration` entity, which inherits from:
    - ConcentrationLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_47287d09_6108_45ca_ac65_8b9451b1065e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaximumConcentration'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaximumConcentration(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_47287d09_6108_45ca_ac65_8b9451b1065e',
    
    class_name='MaximumConcentration',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_47287d09_6108_45ca_ac65_8b9451b1065e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaximumConcentration',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    